data_type_list = ["\'b", "\'d","\'h"]


class DataConvert:

    def data_to_int(data, convert_mode):
        # [data : str] [convert_mode : int]
        if convert_mode == 1:
            return int(data)
        elif convert_mode == 0:
            return int(data,2)
        elif convert_mode == 2:
            return int(data,16)
        else:
            # invalid data
            return -1

    def int_to_data(data, data_type):
        result = ''
        if data_type == 0:
            result = format(data, 'b')
        elif data_type == 1:
            result = str(data)
        elif data_type == 2:
            result = format(data,'X')

        return result

    def is_verilog_format(data):
        if "'" in data:
            return True
        return False

    def get_data_header(data, part='ALL'):
        result = ""
        if data.is_verilog_format(data):
            for dtl in data_type_list:
                if dtl in data:
                    result = data[:data.find(dtl)+len(dtl)]

            if part == 'BIT':
                result = result.split("'")[0]
            elif part == 'TYPE':
                result = result.split("'")[1]
            elif part == 'ALL':
                pass
            else:
                print('err')

        return result

    def data_convert(data, target_type=2, form=0):
        # TBD verifying data
        data = str(data)
        header = ''
        data_length = -1
        # remove space, underscore
        data = data.replace(" ","")
        data = data.replace("_","")

        target_type = int(target_type)
        dataType = 1

        # TBD : Data length verify
        if data.is_verilog_format(data):
            for i in range(len(data_type_list)):
                # TBD : check invalid data Type
                if data_type_list[i] in data:
                    tmp_type = data_type_list[i]
                    # extract value
                    data_header_index = data.find(tmp_type)
                    if data_header_index > 0:
                        data_length = int(data[:data_header_index])
                    data = data[data_header_index + len(tmp_type):]
                    break

        int_data = data.data_to_int(data, dataType)
        if data_length == -1:
            data_length = len(format(int_data,'b'))

        result_data = data.int_to_data(int_data, target_type)
        if form == 0:
            # default form [ ex : 4'b1001 ]
            header = str(data_length) + data_type_list[target_type]
        else:
            # just data [ ex : 1001 ]
            header = ''

        result_data = header + str(result_data)

        return result_data

# test function
def main(data_convert=None):
    import sys
    if len(sys.argv) > 1:
        data = sys.argv[1]
    else:
        data = input('input for convert number: ')

    if len(sys.argv) > 2:
        data_type = int(sys.argv[2])
    else:
        data_type = int(input('input for convert type: '))

    if len(sys.argv) > 3:
        target_type = int(sys.argv[3])
    else:
        target_type = int(input('input for return type: '))
    print(data_convert(data, data_type, target_type))

if __name__ == "__main__":
    main()



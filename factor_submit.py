class FactorHandler:
    my_time = {}
    def __init__(self):
        pass

    def add_factor(self, time_format, time, value):
        time_format_ = time_format.split('/')
        time_ = time.split('/')
        time_standard = tuple(sorted(list(zip(time_format_, time_))))
        if time_standard in self.my_time.keys():
            self.my_time[time_standard] += value
        else:
            self.my_time[time_standard] = value
        
    def remove_all_factors(self, time_format, time):
        time_format_ = time_format.split('/')
        time_ = time.split('/')
        time_standard = tuple(sorted(list(zip(time_format_, time_))))
        del self.my_time[time_standard]

    def get_sum(self, time_format, start_time, finish_time):
        time_format_ = time_format.split('/')
        time_start = start_time.split('/')
        time_finish = finish_time.split('/')

        s_f_time = sorted(list(zip(time_format_, time_start, time_finish)))

        for index_,item in enumerate(s_f_time):
            if index_ == 0:
                day_s = int(item[1])
                day_f = int(item[2])
            elif index_ == 1:
                month_s = int(item[1])
                month_f = int(item[2])
            else:
                year_s = int(item[1])
                year_f = int(item[2])
                
        list_ = []
        sum_ = 0
        for k, v in self.my_time.items():
            if year_s <= int(k[2][1]) <= year_f:           # year
                if month_s <= int(k[1][1]) <= month_f:     # month
                    if day_s <= int(k[0][1]) <= day_f:     # day
                        list_.append(k)
        
        for k in list_:
            sum_ += int(self.my_time.get(k))

        return sum_


'''
instances:
'''

fh = FactorHandler()
fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)  # add factor in this time
fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)  # add factor in this time
fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)  # add factor in this time
fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)   # add factor in this time
fh.remove_all_factors("mm/dd/yyyy", "10/03/2019") # remove factor in this time
answer = fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/05/10") # sum factor price start time to end time.
print(answer)

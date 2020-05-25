import numpy


class Target:
    def __init__(self, hash_dict):
        self.hash_dict = hash_dict
        self.fill = {}

    @property
    def target_property(self):
        for freq in list(self.hash_dict.keys()):
            self.fill.update({freq - list(self.hash_dict.keys())[0]: [t - self.hash_dict[freq][0] for t in
                                                                      self.hash_dict[freq]]})
        return self.fill

    def __eq__(self, other):
        if len(self.target_property) > len(other.target_property):
            main = other.target_property
            seconder = self.target_property
        else:
            main = self.target_property
            seconder = other.target_property

        counter = 0
        fin_counter = 0
        for target_hash_1 in list(main.keys()):
            for element in main[target_hash_1]:
                for sec_element in seconder[target_hash_1]:
                    if sec_element * 0.7 < element < sec_element * 1.3:
                        counter += 1
                        break
                fin_counter += 1
        if fin_counter == 0:
            return False
        if counter / fin_counter > 0.9:
            return True
        else:
            return False






class Cutter:
    def __init__(self, hash_table):
        self.hash_table = hash_table
        self.t_frame = 5
        self.t_step = 2.5
        self.f_frame = 400
        self.f_step = 200
        self.cut_element = []
        self.hash_dict = {}

    def cut_and_create_target(self):
        for element in self.hash_table:
            if element[1] in list(self.hash_dict.keys()):
                self.hash_dict[element[1]].append(element[0])
            else:
                self.hash_dict.update({element[1]: []})
        current_f = numpy.amin(self.hash_table, axis=0)[1]
        while current_f <= list(self.hash_dict.keys())[-1] - self.t_frame:
            current_t = 0
            while current_t <= numpy.amax(self.hash_table, axis=0)[0] - self.t_frame:
                hash_dict = {}
                for i in range(int(current_f), int(current_f) + self.f_frame, 100):
                    if i > list(self.hash_dict.keys())[-1] - self.t_frame:
                        break
                    self.hash_dict.setdefault(i, [0])
                    hash_dict.update({i: [element for element in self.hash_dict[i] if current_t <= element < current_t +
                                          self.t_frame]})
                current_t += self.t_step
                self.cut_element.append(Target(hash_dict))
            current_f += self.f_step

    def get_cut_element(self):
        return self.cut_element

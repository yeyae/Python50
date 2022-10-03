#클래스 상속(Python49와 이어서)
class MoreFourCal(FourCal):
    pass

#클래스 상속 양식
#class 클래스 이름(상속할 클래스 이름)
a = MoreFourCal(4,2)
a.add()

#a의 b제곱을 계산하는 MoreFourCal클래스 만들기
class MoreFouCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
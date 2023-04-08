import smartpy as sp

class AddSub(sp.Contract):
    def __init__(self,value):
        #storage of all variables in a contract
        self.init(
           
             num_a =sp.int(5),
             num_b = sp.int(3),
             addition_result=value,
             sub_result=0
             
        )
       
    @sp.entry_point
    def adding(self,params):
        sp.set_type(params,sp.TRecord(x=sp.TInt,y=sp.TInt))
        self.data.addition_result=self.data.num_a + self.data.num_b

    @sp.entry_point
    def sub(self,params1):
        sp.set_type(params1, sp.TRecord(a=sp.TInt,b=sp.TInt))
        self.data.sub_result=params1.a - params1.b

@sp.add_test(name="main")
def test():
    # Creating a sceanrio
    scenario = sp.test_scenario()

    # crreating an instance of class
    in1=AddSub(6)
    scenario += in1

    #calling the function / entry point 
    scenario += in1.adding(x=5,y=55)
    subsce=AddSub(7)
    scenario += subsce
    scenario += subsce.sub(a=1,b=-2)
    
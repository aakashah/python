class Chassis(UcsObject):

    meta = EquipmentChassis
    class_id = NamingId.EQUIPMENT_CHASSIS

    def __init__(self, ucs, chassis):
        dn = 'sys/chassis-%s' % chassis
        super(Chassis, self).__init__(hdl=ucs,
                                      dn=dn,
                                      class_id=self.class_id)

        self.__dict__['chassis'] = chassis

    def do_reacknowledge(self):
        self.AdminState = "re-acknowledge"

    def do_remove(self):
        self.AdminState = "remove"

    def do_decommission(self):
        self.AdminState = "decommission"

    def do_recommission(self):
        c = filter(lambda m: m.EpDn == self.dn, self.list_all())[0]
        c.AdminState = 'enabled'

    def list_all(self):
        fabric = self.hdl.find(class_id=NamingId.FABRIC_DCE_SRV)[0]
        return fabric.find(class_id=NamingId.FABRIC_SW_CH_PH_EP)
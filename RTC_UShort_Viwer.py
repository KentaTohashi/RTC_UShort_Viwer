#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RTC_UShort_Viwer.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time

sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.DEBUG)

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
rtc_ushort_viwer_spec = ["implementation_id", "RTC_UShort_Viwer",
                         "type_name", "RTC_UShort_Viwer",
                         "description", "ModuleDescription",
                         "version", "1.0.0",
                         "vendor", "Kenta Tohashi",
                         "category", "Category",
                         "activity_type", "STATIC",
                         "max_instance", "1",
                         "language", "Python",
                         "lang_type", "SCRIPT",
                         ""]


# </rtc-template>

##
# @class RTC_UShort_Viwer
# @brief ModuleDescription
# 
# 
class RTC_UShort_Viwer(OpenRTM_aist.DataFlowComponentBase):

    ##
    # @brief constructor
    # @param manager Maneger Object
    #
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_input = OpenRTM_aist.instantiateDataType(RTC.TimedUShort)
        """
        """
        self._inputIn = OpenRTM_aist.InPort("input", self._d_input)

    # initialize of configuration-data.
    # <rtc-template block="init_conf_param">

    # </rtc-template>

    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # formaer rtc_init_entry()
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onInitialize(self):
        # Bind variables and configuration variable

        # Set InPort buffers
        self.addInPort("input", self._inputIn)

        # Set OutPort buffers

        # Set service provider to Ports

        # Set service consumers to Ports

        # Set CORBA Service Ports

        return RTC.RTC_OK

    ###
    ##
    ## The finalize action (on ALIVE->END transition)
    ## formaer rtc_exiting_entry()
    ##
    ## @return RTC::ReturnCode_t
    #
    ##
    # def onFinalize(self):
    #
    #	return RTC.RTC_OK

    ###
    ##
    ## The startup action when ExecutionContext startup
    ## former rtc_starting_entry()
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    # def onStartup(self, ec_id):
    #
    #	return RTC.RTC_OK

    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ## former rtc_stopping_entry()
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    # def onShutdown(self, ec_id):
    #
    #	return RTC.RTC_OK

    ##
    #
    # The activated action (Active state entry action)
    # former rtc_active_entry()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        self.CO2 = np.zeros(1)
        plt.figure()
        self.lines, = plt.plot(np.arange(1), self.CO2)
        return RTC.RTC_OK

    ##
    #
    # The deactivated action (Active state exit action)
    # former rtc_active_exit()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
        return RTC.RTC_OK

    ##
    #
    # The execution action that is invoked periodically
    # former rtc_active_do()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        if self._inputIn.isNew():
            self._d_input = self._inputIn.read()
            self.CO2 = np.append(self.CO2, self._d_input.data)
            if len(self.CO2) > 50:
                self.CO2 = np.delete(self.CO2, 0)
            print self.CO2
            self.lines.set_data(np.arange(len(self.CO2)), self.CO2)
            plt.xlim(0, len(self.CO2) + 2)
            plt.ylim(self.CO2.min() - 50, self.CO2.max() + 50)
            print "draw start"
            plt.draw()
            print "draw end"
            plt.pause(0.01)
        return RTC.RTC_OK

###
##
## The aborting action when main logic error occurred.
## former rtc_aborting_entry()
##
## @param ec_id target ExecutionContext Id
##
## @return RTC::ReturnCode_t
##
##


# def onAborting(self, ec_id):
#
#	return RTC.RTC_OK

###
##
## The error action in ERROR state
## former rtc_error_do()
##
## @param ec_id target ExecutionContext Id
##
## @return RTC::ReturnCode_t
##
##
# def onError(self, ec_id):
#
#	return RTC.RTC_OK

###
##
## The reset action that is invoked resetting
## This is same but different the former rtc_init_entry()
##
## @param ec_id target ExecutionContext Id
##
## @return RTC::ReturnCode_t
##
##
# def onReset(self, ec_id):
#
#	return RTC.RTC_OK

###
##
## The state update action that is invoked after onExecute() action
## no corresponding operation exists in OpenRTm-aist-0.2.0
##
## @param ec_id target ExecutionContext Id
##
## @return RTC::ReturnCode_t
##

##
# def onStateUpdate(self, ec_id):
#
#	return RTC.RTC_OK

###
##
## The action that is invoked when execution context's rate is changed
## no corresponding operation exists in OpenRTm-aist-0.2.0
##
## @param ec_id target ExecutionContext Id
##
## @return RTC::ReturnCode_t
##
##
# def onRateChanged(self, ec_id):
#
#	return RTC.RTC_OK


def RTC_UShort_ViwerInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=rtc_ushort_viwer_spec)
    manager.registerFactory(profile,
                            RTC_UShort_Viwer,
                            OpenRTM_aist.Delete)


def MyModuleInit(manager):
    RTC_UShort_ViwerInit(manager)

    # Create a component
    comp = manager.createComponent("RTC_UShort_Viwer")


def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == "__main__":
    main()

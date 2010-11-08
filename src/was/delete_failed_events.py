import javax.management as mgmt 
import time

AdminControl.trace( 'com.ibm.wbimonitor.*=all=enabled' )

################################################
# Start doing work 
################################################

# Set these variables to the correct values
# Replace <modelID> with the value of the Model column displayed in the 
# administrative console and <versionDate> with the model version date, 
# in the format YYYYMMDDHHMMSS.

#myModel = '<modelID>'
#myVersion = ' <versionDate>'

myModel = 'TestMonitor_MM3'
myVersion = '20101020112930'

eqmb = AdminControl.queryNames('WebSphere:type=ErrorQ,*')
modelVer = AdminControl.invoke(eqmb, 'getModelVersion', '[' + myModel + ' ' + myVersion + ']')
print 'modelVer= '
print modelVer
temp1 = modelVer.split('[')[1]
modelDBID = temp1.split(']')[0]
print 'modelDBID='
print modelDBID
eqObjNameString = AdminControl.completeObjectName('WebSphere:type=ErrorQ,*') 
eqObjName = mgmt.ObjectName(eqObjNameString) 

## Begin delete failed events ##                  
#instancesByDBID = AdminControl.invoke(eq, 'listFailedInstances', '[' + modelDBID + ']').split(lineSeparator)                  
instancesByDBID = AdminControl.invoke(eqmb, 'listFailedInstances', '[' + modelDBID + ']').split(lineSeparator)                  
for instance in instancesByDBID :
    instance = instance.split('[')[1]
    instance = instance.split(']')[0]
    print "instance=", instance
    #eventIds = AdminControl.invoke(eq, 'listFailedEventIds', '[' + instance + ']').split(lineSeparator)
    eventIds = AdminControl.invoke(eqmb, 'listFailedEventIds', '[' + instance + ']').split(lineSeparator)
    print "eventIds=", eventIds
    for eventId in eventIds :
        if eventId != '' :
            print "delete ", eventId
            #AdminControl.invoke(eq, 'deleteEvents', '[' + instance + ' ' + eventId + ']')
## End delete failed events ##

## Begin delete failed instances ##
# Get the MBean
import javax.management as mgmt 
eqObjNameString = AdminControl.completeObjectName('WebSphere:type=ErrorQ,*') 
eqObjName = mgmt.ObjectName(eqObjNameString)

# Pass the model DBID as the parm
parms = [ modelDBID ] 
signature = ['java.lang.String'] 
instList = AdminControl.invoke_jmx(eqObjName, 'listFailedInstances', parms, signature)

# Loop through the list of InstanceBeans
if instList != None:
    for inst in instList:
        rootInstId = inst.getRootInstanceId()
        #rootInstId = rootInstId.replace(";", ";")
        print "rootInstId=", rootInstId
        AdminControl.invoke(eqmb, 'resetEventSequenceInstance', '["' + myModel + '" ' + myVersion + ' "' + rootInstId + '"]')
## End delete failed instances ##


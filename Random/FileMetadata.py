import MetadataModule


propgenerator= MetadataModule.property_sets('C:/Users/wyatt/Downloads/chapter.wav')
for name, properties in propgenerator:
    print ""
    for k, v in properties.items ():
        if(k == 'PIDSI_AUTHOR'):
            print v
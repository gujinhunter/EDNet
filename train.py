from ednet import EDNet

# Build a model from scratch (choose from: t,n,s,m,b,l,x)
model = EDNet("./ednet/cfg/models/ednet/ednet-t.yaml") 
# Train the model
model.train(data="visdrone-det.yaml", epochs=200, imgsz=640) 
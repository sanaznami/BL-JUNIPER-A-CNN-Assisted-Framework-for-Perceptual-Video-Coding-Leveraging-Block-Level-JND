%% Temporal Perceptual Information (TPI) of frame

%Path of bmp frames
Path = 'D:\PHD\MCL-JCV\BMPFrames\SRC30\Raw\';
NumPath=dir([Path '*.bmp']);
LenPath=length(NumPath)

%Calculating TPI
for k=1:LenPath
    imgname = [ Path NumPath(k).name ];
    Frame=imread(imgname);
    GFrame{k,1}=rgb2gray(Frame);
end

TPI_Frame=[];
for k=2:size(GFrame,1)
    for i=1:size(Frame,1)
        for j=1:size(Frame,2)
            MotionDiff{k,1}(i,j)=GFrame{k,1}(i,j)-GFrame{k-1,1}(i,j);
        end
    end
    TPI_Frame(k,1)=std2(MotionDiff{k,1});
end

NumberofFrame=5;
for i=1:size(TPI_Frame,1)/NumberofFrame
    TPI_Frame((i-1)*NumberofFrame+1,2)=max(TPI_Frame((i-1)*NumberofFrame+1:i*NumberofFrame,1));
end

%% TPI of blocks

Block_Size=64;
for k=2:size(MotionDiff,1)
    for s=1:size(Frame,1)/Block_Size
        for z=1:size(Frame,2)/Block_Size
            BlockLevelTPI{k,1}(s,z)=std2(MotionDiff{k,1}(Block_Size*(s-1)+1:s*Block_Size,Block_Size*(z-1)+1:z*Block_Size));
        end
    end
end
 
for k=2:size(MotionDiff,1)
    for h=1:size(Frame,2)/Block_Size
        BlockLevelTPI{k,1}(s+1,h)=std2(MotionDiff{k,1}(Block_Size*s+1:size(Frame,1),Block_Size*(h-1)+1:h*Block_Size));
    end
end

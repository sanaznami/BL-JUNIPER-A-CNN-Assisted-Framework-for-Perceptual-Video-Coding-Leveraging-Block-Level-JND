%% SSIM of frames

%Path of Reference bmp frames
Path = 'D:\PHD\MCL-JCV\BMPFrames\SRC01\Raw\';
NumPath=dir([Path '*.bmp']);
LenPath=length(NumPath)

%Reading Reference bmp frames
for i= 1 :LenPath
    imgname = [ Path NumPath(i).name ];
    Frame{i,1}=imread(imgname);
end

%Path of bmp frames of ith JND level
JNDPath = 'D:\PHD\MCL-JCV\BMPFrames\SRC01\DistortedFrame\26\';
NumJNDPath=dir([JNDPath '*.bmp']);
LenJNDPath=length(NumJNDPath)

%Reading JND bmp frames
for i= 1 :LenJNDPath
    JNDimgname = [ JNDPath NumJNDPath(i).name ];
    JNDFrame{i,1}=imread(JNDimgname);
end

for i= 1 :LenPath
    SSIMJNDFrame(i,1)=ssim(Frame{i,1},JNDFrame{i,1});
end

%% SSIM of blocks
Block_Size=64;
for k=1:LenPath
    for s=1:size(Frame{1,1},1)/Block_Size
        for z=1:size(Frame{1,1},2)/Block_Size
            BlockLevelSSIM{k,1}(s,z)=ssim(JNDFrame{k,1}(Block_Size*(s-1)+1:s*Block_Size,Block_Size*(z-1)+1:z*Block_Size,1:3),Frame{k,1}(Block_Size*(s-1)+1:s*Block_Size,Block_Size*(z-1)+1:z*Block_Size,1:3));
        end
    end
end

for k=1:LenPath
    for h=1:size(Frame{1,1},2)/Block_Size
        BlockLevelSSIM{k,1}(s+1,h)=ssim(JNDFrame{k,1}(Block_Size*(s-1)+1:size(Frame{1,1},1),Block_Size*(h-1)+1:h*Block_Size,1:3),Frame{k,1}(Block_Size*(s-1)+1:size(Frame{1,1},1),Block_Size*(h-1)+1:h*Block_Size,1:3));
    end
end
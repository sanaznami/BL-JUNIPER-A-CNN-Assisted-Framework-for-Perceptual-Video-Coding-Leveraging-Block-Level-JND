clear

%Reading a video
Video = VideoReader('D:\PHD\MCL-JCV\Videos\1080PAVCFQPvideoSRC01-20200915T061845Z-001\1080PAVCFQPvideoSRC01\videoSRC01_01.mp4');

%Extracting all frame of video
AllFrame = read(Video,[1 Inf]);

%extracting one frame of a video every 30 frames
for k=1:30:size(AllFrame,4)
    Frames{floor(k/30)+1,1}=AllFrame(:,:,:,k);
end

%Generating 64*64 blocks
for i=1:16
    for j=1:30
        Blocks{i,j}=Frames{1,1}(64*(i-1)+1:i*64,64*(j-1)+1:j*64,:);
    end
end

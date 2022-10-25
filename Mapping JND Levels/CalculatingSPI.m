%% Spatial Perceptual Information (SPI) of frame

%Path of bmp frames
Path = 'D:\PHD\MCL-JCV\BMPFrames\SRC01\Raw\';
NumPath=dir([Path '*.bmp']);
LenPath=length(NumPath)

%Calculating Sobel Filter
for k=1:LenPath
        imgname = [ Path NumPath(k).name ];
        Frame=imread(imgname);
        GFrame{k,1}=rgb2gray(Frame);
        GFrame{k,1}=double(GFrame{k,1});
end

Im={};
for k=1:size(GFrame,1)
    Im{k,1}(1:size(GFrame{1,1},1)+2,1:size(GFrame{1,1},2)+2)=0;
end

for k= 1:size(GFrame,1)
    for i=1:size(GFrame{1,1},1)
        for j=1:size(GFrame{1,1},2)
            Im{k,1}(i+1,j+1)=GFrame{k,1}(i,j);
        end
    end
end

for k=1:size(Im,1)
    for i=2:size(Im{1,1},1)-1
        for j=2:size(Im{1,1},2)-1
            Gx=((2*Im{k,1}(i+1,j)+Im{k,1}(i+1,j-1)+Im{k,1}(i+1,j+1))-(2*Im{k,1}(i-1,j)+Im{k,1}(i-1,j-1)+Im{k,1}(i-1,j+1)));
            Gy=((2*Im{k,1}(i,j+1)+Im{k,1}(i-1,j+1)+Im{k,1}(i+1,j+1))-(2*Im{k,1}(i,j-1)+Im{k,1}(i-1,j-1)+Im{k,1}(i+1,j-1)));
            Sobel{k,1}(i-1,j-1)=sqrt(Gx.^2+Gy.^2);
        end
    end
end

%Calculating SPI
for k=1:size(Im,1)
    SPI_Frame(k,1)=std2(Sobel{k,1});
end

%% SPI of blocks

Block_Size=64;
for k=1:LenPath
    for s=1:size(Sobel{1,1},1)/Block_Size
        for z=1:size(Sobel{1,1},2)/Block_Size
            BlockLevelSPI{k,1}(s,z)=std2(Sobel{k,1}(Block_Size*(s-1)+1:s*Block_Size,Block_Size*(z-1)+1:z*Block_Size));
        end
    end
end
 
for k=1:LenPath
    for h=1:size(Sobel{1,1},2)/Block_Size
        BlockLevelSPI{k,1}(s+1,h)=std2(Sobel{k,1}(Block_Size*s+1:size(Sobel{1,1},1),Block_Size*(h-1)+1:h*Block_Size));
    end
end

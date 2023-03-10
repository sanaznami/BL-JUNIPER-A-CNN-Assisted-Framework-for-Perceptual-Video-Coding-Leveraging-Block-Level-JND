%%Preparing Block-level Data

%Path of bmp frames
%frame-size: 1920*1080
Path = '';
NumPath=dir([Path '*.bmp']);
LenPath=length(NumPath)

%Reading the frames
for k=1:LenPath
        imgname = [ Path NumPath(k).name ];
        AllFrame{k,1}=imread(imgname);
end

%Creating block-level data
for k=1:LenPath
    for i=1:16
        for j=1:30
            Block{k,1}{i,j}=AllFrame{k,1}(64*(i-1)+1:i*64,64*(j-1)+1:j*64,:);
        end
    end
end

%each blocks in one row
for q=1:LenPath
    for x=1:16
        for y=1:30
            for i=1:64  %block-size=64
               for j=1:64
                   for k=1:3
                      BlockData((q-1)*480+(x-1)*30+y,(k-1)*64*64+(i-1)*64+j)=Block{q,1}{x,y}(i,j,k);
                   end
               end
            end
        end
    end
end

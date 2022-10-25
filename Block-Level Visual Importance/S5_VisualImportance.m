% loading generated saliency from X. Li, H. Lu, L. Zhang, X. Ruan, and M.-H. Yang, "Saliency Detection via Dense and Sparse Reconstruction," pp. 2976–2983, 2013.
% frame-size is 1920*1080
load saliency
Sal=saliency;

% calculating saliency for each block
block_size=64;
for s=1:size(Sal,1)/block_size
    for z=1:size(Sal,2)/block_size
        Smap(s,z)=sum(sum(Sal(block_size*(s-1)+1:s*block_size,block_size*(z-1)+1:z*block_size)))/(block_size*block_size);
    end
end 
for h=1:size(Sal,2)/block_size
    Smap(s+1,h)=sum(sum(Sal(block_size*s+1:size(Sal,1),block_size*(h-1)+1:h*block_size)))/(block_size*(size(Sal,1)-block_size*s));
end

% calculating min and max value
MinSaliency=min(min(Smap))
MaxSaliency=max(max(Smap))

% Normalization
for j=1:size(Smap,2)
    for i=1:size(Smap,1)
        MinMaxSaliency(i,j)=1*(Smap(i,j)-MinSaliency)/(MaxSaliency-MinSaliency);
    end
end

% calculating visual importance value
for b=1:size(MinMaxSaliency,1)
    for c=1:size(MinMaxSaliency,2)
        if MinMaxSaliency(b,c)>=0.5
            VI(b,c)=3;
        else if MinMaxSaliency(b,c)<0.5 && MinMaxSaliency(b,c)>=0.05
                VI(b,c)=2;
            else VI(b,c)=1;
            end
        end
    end
end
 
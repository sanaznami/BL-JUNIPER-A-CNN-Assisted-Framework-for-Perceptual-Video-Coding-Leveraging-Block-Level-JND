%% Perceptual Quality Degradation (PQD)

a=4;
b=0.1;
% load BlockLevelSPI
% load BlockLevelTPI
% load BlockLevelSSIM

% % Calculating Normalized Spatial Complexity(NSC) & Normalized Temporal Complexity(NTC)
% for k=1:5:size(BlockLevelSPI,1)
%     for i=1:17
%         for j=1:30
%             NSC{floor(k/5)+1,1}(i,j)=((BlockLevelSPI{k,1}(i,j))-min(min(BlockLevelSPI{k,1})))/(max(max(BlockLevelSPI{k,1}))-min(min(BlockLevelSPI{k,1})));
%             NTC{floor(k/5)+1,1}(i,j)=((BlockLevelTPI{k,1}(i,j))-min(min(BlockLevelTPI{k,1})))/(max(max(BlockLevelTPI{k,1}))-min(min(BlockLevelTPI{k,1})));
%         end
%     end
% end

% Calculating Normalized Spatial Complexity(NSC) & Normalized Temporal Complexity(NTC)
for k=1:size(BlockLevelSPI,1)
    for i=1:17
        for j=1:30
            NSC{k,1}(i,j)=((BlockLevelSPI{k,1}(i,j))-min(min(BlockLevelSPI{k,1})))/(max(max(BlockLevelSPI{k,1}))-min(min(BlockLevelSPI{k,1})));
            NTC{k,1}(i,j)=((BlockLevelTPI{k,1}(i,j))-min(min(BlockLevelTPI{k,1})))/(max(max(BlockLevelTPI{k,1}))-min(min(BlockLevelTPI{k,1})));
        end
    end
end

% Calculating Perceptual Information (PI)
for k=1:size(NSC,1)
    for i=1:17
        for j=1:30
            PI{k,1}(i,j)=NTC{k,1}(i,j)/NSC{k,1}(i,j);
        end
    end
end

% Calculating Perceptual Quality Degradation (PQD)
for k=1:size(PI,1)
    for i=1:17
        for j=1:30
            PQD{k,1}(i,j)=(a*PI{k,1}(i,j)+b)*(1-BlockLevelSSIM{k,1}(i,j));
        end
    end
end
load VI
load PredictedJND %generated from python file
load 
TargetQP=22; % determine the target QP

for i=1:size(PredictedJND,1)
     if TargetQP>PredictedJND(i,3)
         JND(i,1)=TargetQP;
     else if TargetQP<=PredictedJND(i,1) && VI(i,1)==3
        JND(i,1)=PredictedJND(i,1);
    else if TargetQP<=PredictedJND(i,1) && VI(i,1)==2
           JND(i,1)=PredictedJND(i,2);
        else if TargetQP<=PredictedJND(i,1) && VI(i,1)==1
               JND(i,1)=PredictedJND(i,3);
            else if PredictedJND(i,1)<TargetQP && TargetQP<=PredictedJND(i,2) && VI(i,1)==3
                    JND(i,1)=PredictedJND(i,2);
                else if PredictedJND(i,1)<TargetQP && TargetQP<=PredictedJND(i,2) && VI(i,1)==2
                        JND(i,1)=PredictedJND(i,3);
                    else if PredictedJND(i,1)<TargetQP && TargetQP<=PredictedJND(i,2) && VI(i,1)==1
                            JND(i,1)=PredictedJND(i,3);
                        else if PredictedJND(i,2)<TargetQP && TargetQP<=PredictedJND(i,3) && VI(i,1)==3
                                JND(i,1)=PredictedJND(i,3);
                            else if PredictedJND(i,2)<TargetQP && TargetQP<=PredictedJND(i,3) && VI(i,1)==2
                                    JND(i,1)=PredictedJND(i,3);
                                else if PredictedJND(i,2)<TargetQP && TargetQP<=PredictedJND(i,3) && VI(i,1)==1
                                        JND(i,1)=PredictedJND(i,3);
                                    else JND(i,1)=PredictedJND(i,3);
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    end
 end
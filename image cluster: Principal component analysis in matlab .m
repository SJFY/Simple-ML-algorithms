num = 1;
for i = 1:10000
    if(labels(i) == 2)  % change different class no.
        class(num,:) = data(i,:);
        num = num+1;
    end
end
%get means inside this class
means = mean(class,1);
%subtract means
[r,c]=size(class);
class = double(class);
for i = 1:r
    submean(i,:) = class(i,:)-means;
end
%get conv matrix
covmat = (submean'*submean);
[evt,evl]=eig(covmat);
%get error
 for k = 1:20
            pc(:,k)=evt(:,3072-k+1);
           
 end
 xi = 0;
 
        for m = 1:20
            xi = submean * pc(:,m) * pc(:,m)'+xi;
            
        end
        [ra,ca] = size(xi);
       
      
        error = 0;
        for m = 1: ra
            error = norm(submean(m,:)-(xi(m,:)+means))/ra + error;
        end
for j = 1: 10
num = 1;
for i = 1:10000
    if(labels(i) == j-1)  % change different class no.
        class(num,:) = data(i,:);
        num = num+1;
    end
end
%get means inside this class
means(j,:) = mean(class,1);
end
%so far, we get the matrix of each mean image, we can make a mean image matrix as distance matrix
%use principal coordinate analysis to get the 2D map of of high dimension distance matrix
%at the same time maintain the distance between each class mean image. 
conv = (means*means');
[evt,evl]=eig(conv);
u = zeros(10);
A = zeros(10);
u(:,1) = evt(:,10);
u(:,2) = evt(:,10);
A(1,1) = sqrt(evl(10,10));
A(2,2) = sqrt(evl(9,9));
v = u*A;
scatter(v(:,1))

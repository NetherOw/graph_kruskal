library("tidyverse")
library(effects)
data_lists <- read_csv("D:\\Python projects\\runtime.csv")
data_matrices <- read_csv("C:\\Users\\ceoet\\Downloads\\Telegram Desktop\\seeassveev2.csv", col_names = c("nVertices","density","runtime"))
data <- left_join(data_lists,data_matrices, by = join_by(nVertices,density))%>%
  mutate(list = runtime.x,matrix = runtime.y*1000)%>%
  select(nVertices,density,list,matrix)%>%
  pivot_longer(c(list,matrix), names_to = "type", values_to = "runtime")

runtime_to_density <- data%>%
  group_by(density,type)%>%
  summarise(mean_runtime = mean(runtime))
ggplot(runtime_to_density)+
  geom_point(aes(density, mean_runtime, colour = type))+
  geom_smooth(aes(density, mean_runtime, colour = type))+
  labs(title = "Залежність від щільності",y ="Час (сек*1000)", x = "Щільність")
runtime_to_nVertices <- data%>%
  group_by(nVertices, type)%>%
  summarise(mean_runtime = mean(runtime))
ggplot(runtime_to_nVertices)+
  geom_point(aes( nVertices,mean_runtime,colour = type))+
  geom_smooth(aes(nVertices,mean_runtime,  colour =type))+
  labs(title = "Залежність від кількості вершин",y ="Час (сек*1000)", x = "Кількість вершин")

ggplot(runtime_to_nVertices%>%filter(type == "list"))+
  geom_point(aes( nVertices,mean_runtime,colour = type))+
  geom_smooth(aes(nVertices,mean_runtime,  colour =type))+
  labs(title = "Залежність від кількості вершин",y ="Час (сек*1000)", x = "Кількість вершин")
 

data_matrix <- read_csv()

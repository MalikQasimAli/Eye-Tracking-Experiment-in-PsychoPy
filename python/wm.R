source('custom.R')

load.libraries(c('emmeans','sciplot','ez','psych','reshape','plyr','ggplot2','afex','dplyr','pastecs'))

source("tmcustom.R") 
source("lwheatmap.R") 
source("WMSP.R") 

df <- read.csv("fxtn-aois.csv")
# ===========
# KK code:
# +=========
# filter out outlying fixations
fout <- boxplot(df$duration, plot = FALSE)$out
# statistics of outlying fixations
length(fout)
dim(df)[1]
length(fout)/dim(df)[1]

df <- df %>% 
	filter(!duration %in% fout)



# select condition we need
dd <- df[which(df$exp_id == "tcq" | df$exp_id == "tsq"), ]

# figure out diemnsions of 1D WM will be, e.g., -18,...17
smin <- min(dd$aoi_span)
smax <- max(dd$aoi_span)

# -- looping over individual ---------------------------------------------
den <- data.frame()
for(i in unique(dd$subj)){
	ddf <- dd[which(dd$subj == i), ]
    M <- zeroWM(smin,smax)
    TransWMatrix(M,data=ddf,
                  StimulusVar="stim",
                  SubjectsVar="subj",
                  SpanVar="aoi_span")
    TransEntropy(M, data=ddf,
                  StimulusVar="stim",
                  SubjectsVar="subj",
                  SpanVar="aoi_span")
    TMentrop$subj = i 
	den <- rbind(den, TMentrop)
    TransWPlot2(transMatrix=M,
             plotName=paste0("./figs/","WM_subj",i,".pdf"),
             plotColors=brewer.pal(9,"Oranges"),
             # title=paste0("subject", i, "stimuli_"),
             annColor='black')
}

save(den, file = "wm.rda")

#  ===================================




# =============
# ATD code:
# ============
# figure out diemnsions of 1D WM will be, e.g., -18,...17
# smin <- min(df$aoi_span)
# smax <- max(df$aoi_span)
#
# # -- looping over individual ---------------------------------------------
#
# # ddf <- df[which(df$exp_id == "tcq"),]
# uniqS <- unique(df$subj)
# M_ <- list()
# en_ <- list()
# for (i in 1:23) {
#
#   # select for individual subject
#   ddf <- df[which(df$exp_id == "tcq" & df$subj == uniqS[i]), ]
#
#   # some debugging
#   print(sprintf("Subject: %s",uniqS[i]))
#   M <- zeroWM(smin,smax)
#   M_[[i]] <- TransWMatrix(M,data=ddf,
#                     StimulusVar="stim",
#                     SubjectsVar="subj",
#                     SpanVar="aoi_span")
#   M_[[i]] <- M
#   print(sprintf("M_[[%d]]",i))
#   print(M_[[i]])
#   en_[[i]] <- TransEntropy(M,data=ddf,
#                     StimulusVar="stim",
#                     SubjectsVar="subj",
#                     SpanVar="aoi_span")
#   en_[[i]] <- TMentrop
#   print(sprintf("en_[[%d]]",i))
#   print(en_[[i]])
#   TransWPlot2(transMatrix=M,
#            plotName=paste("./figs/","WM_",uniqS[i],".pdf",sep=""),
#            plotColors=brewer.pal(9,"Oranges"),
#            title="tcq",
#            annColor='black')
# }
#
# # combining all en_ into single data frame
# denc <- data.frame()
# for(i in 1:23){
# 	d <- en_[[i]] %>%
# 	mutate(subj = ifelse(i<10, paste0("P0",i), paste0("P",i)))
# 	denc <- rbind(denc, d)
# }
# denc$block = "code"
#
#
#
# #
# ddf <- df[which(df$exp_id == "tsq"),]
# uniqS <- unique(df$subj)
# M_ <- list()
# en_ <- list()
# for (i in 1:23) {
#
#   # select for individual subject
#   ddf <- df[which(df$exp_id == "tsq" & df$subj == uniqS[i]), ]
#
#   # some debugging
#   print(sprintf("Subject: %s",uniqS[i]))
#   M <- zeroWM(smin,smax)
#   M_[[i]] <- TransWMatrix(M,data=ddf,
#                     StimulusVar="stim",
#                     SubjectsVar="subj",
#                     SpanVar="aoi_span")
#   M_[[i]] <- M
#   print(sprintf("M_[[%d]]",i))
#   print(M_[[i]])
#   en_[[i]] <- TransEntropy(M,data=ddf,
#                     StimulusVar="stim",
#                     SubjectsVar="subj",
#                     SpanVar="aoi_span")
#   en_[[i]] <- TMentrop
#   print(sprintf("en_[[%d]]",i))
#   print(en_[[i]])
#   TransWPlot2(transMatrix=M,
#            plotName=paste("./figs/","WM_",uniqS[i],".pdf",sep=""),
#            plotColors=brewer.pal(9,"Oranges"),
#            title="tcq",
#            annColor='black')
# }
#
# # combining all en_ into single data frame
# dens <- data.frame()
# for(i in 1:23){
# 	d <- en_[[i]] %>%
# 	mutate(subj = ifelse(i<10, paste0("P0",i), paste0("P",i)))
# 	dens <- rbind(dens, d)
# }
# dens$block = "text"
#
#
# den <- rbind(denc, dens)
#
#
#
# save(den, file = "wm_entropy.rda")


# -- picking out per individual ------------------------------------------
M <- zeroWM(smin,smax)

# like block, exp_id: tca, tcq, tsa, tsq
# like trial, ses_id: 1, 2, 3, 4, 5
#ddf <- df[which(df$stim == "tcq01"), ] # select stim
ddf <- df[which(df$stim == "tsq04" & df$subj == "P04"), ] # select stim
#ddf
M_tcq01_P18 <- TransWMatrix(M,data=ddf,
                    StimulusVar="stim",
                    SubjectsVar="subj",
                    SpanVar="aoi_span")
M_tcq01_P18 <- M
M_tcq01_P18

en_tcq01_18 <- TransEntropy(M,data=ddf,
                    StimulusVar="stim",
                    SubjectsVar="subj",
                    SpanVar="aoi_span")
en_tcq01_18 <- TMentrop
en_tcq01_18

TransWPlot2(transMatrix=M_tcq01_P18,
           plotName="./figs/WM_tsq04_P04.pdf",
           plotColors=brewer.pal(9,"Oranges"),
           title="tcq",
           annColor='black')


# -- picking out individual conditions: block (tcq or tsq) ---------------
M <- zeroWM(smin,smax)

# like block, exp_id: tca, tcq, tsa, tsq
# like trial, ses_id: 1, 2, 3, 4, 5
ddf <- df[which(df$exp_id == "tcq"), ] # select block
#ddf
M_tcq <- TransWMatrix(M,data=ddf,
                    StimulusVar="ses_id",
                    SubjectsVar="subj",
                    SpanVar="aoi_span")
M_tcq <- M
M_tcq

en_tcq <- TransEntropy(M,data=ddf,
                    StimulusVar="stim",
                    SubjectsVar="subj",
                    SpanVar="aoi_span")
en_tcq <- TMentrop
en_tcq

TransWPlot2(transMatrix=M_tcq,
           plotName="./figs/WM_tcq.pdf",
           plotColors=brewer.pal(9,"Oranges"),
           title="tcq",
           annColor='black')

M <- zeroWM(smin,smax)

# like block, exp_id: tca, tcq, tsa, tsq
# like trial, ses_id: 1, 2, 3, 4, 5
ddf <- df[which(df$exp_id == "tsq"), ] # select block
#ddf
M_tsq <- TransWMatrix(M,data=ddf,
                    StimulusVar="ses_id",
                    SubjectsVar="subj",
                    SpanVar="aoi_span")
M_tsq <- M
M_tsq

en_tsq <- TransEntropy(M,data=ddf,
                    StimulusVar="stim",
                    SubjectsVar="subj",
                    SpanVar="aoi_span")
en_tsq <- TMentrop
en_tsq

TransWPlot2(transMatrix=M_tsq,
           plotName="./figs/WM_tsq.pdf",
           plotColors=brewer.pal(9,"Oranges"),
           title="tsq",
           annColor='black')


# ------------------------------------------------------------------------

# Note: entropy is computed as the empirical entropy, estimated via maximum
#       likelihood, bias-corrected by applying the Miller-Madow correction
#       to the empirical entropy
con_tcq <- c(rep("0",length(en_tcq$Stimulus)))
con_tsq <- c(rep("1",length(en_tsq$Stimulus)))

# construct new data frame
Entropy <- c(en_tcq$Entropy,en_tsq$Entropy)
Stimulus <- c(en_tcq$Stimulus,en_tsq$Stimulus)
Task <- c(con_tcq,con_tsq)
drec <- data.frame(Entropy, Stimulus, Task)

Entropy
Stimulus
Task
drec

# calculate anova
#ezANOVA(data=drec, dv=Entropy, wid=Stimulus, within=Task, type=3)
drec$Stimulus <- factor(drec$Stimulus)
drec$Task <- factor(drec$Task)
attach(drec)
#H.aov <- aov(Entropy ~ (Stimulus * Task) + Error(Stimulus / Task), drec)
#H.aov <- aov(Entropy ~ (Stimulus * Task) + Error(Stimulus), drec)
H.aov <- aov(Entropy ~ Task + Error(Stimulus), drec)
summary(H.aov)
detach(drec)

# doesn't work...missing values
#(fit <- aov_ez(data = drec, id="Stimulus", dv="Entropy", within="Task"))
#summary(fit)
#lsmeans(fit,"Task")

#t.test(drec$Entropy ~ drec$Task)
pairwise.t.test(drec$Entropy, drec$Task, p.adj="bonferroni")
describeBy(drec$Entropy, group=drec$Task)
ddf_0 = drec$Entropy[which(drec$Task == "0")]
ddf_1 = drec$Entropy[which(drec$Task == "1")]
power.t.test(power=.95,sig.level=.05,sd=max(sd(ddf_0),sd(ddf_1)),delta=abs(mean(ddf_0)-mean(ddf_1)))

# ------------------------------------------------------------------------

# Visualisation
# from http://www.r-bloggers.com/using-r-barplot-with-ggplot2/
# rearrange data leaving out the variable of interest (Entropy in this case)
#    Entropy  SEntropy Stimulus   Task
melted <- melt(drec, id.vars=c("Stimulus","Task"))
melted
# compute means of the variable of interest, grouping by cond
means <- ddply(melted,c("Task","variable"),summarise,mean=mean(value))
means
# compute standard error of the mean
entropy.sem <- ddply(melted,c("Task","variable"),summarise,mean=mean(value),
                   sem=sd(value)/sqrt(length(value)))
entropy.sem <- transform(entropy.sem, lower=mean-sem, upper=mean+sem)
entropy.sem
#
plotName <- "./figs/wm_entropies.pdf"
pdf(plotName,family="NimbusSan",useDingbats=FALSE)
ggplot(data=means, aes(x=Task, y=mean, fill=variable)) +
  geom_bar(position=position_dodge(),
           stat="identity",
#          colour="#303030", fill="#606060",
           alpha=.7) +
  geom_errorbar(data=entropy.sem,aes(ymin=lower, ymax=upper),
                width=.2, size=.3,
                position=position_dodge(.9)) + 
  theme_bw(base_size=20) + 
  theme(legend.position = "none") + #turn off the legend
  theme(panel.border=element_blank()) +
  theme(panel.grid.major=element_blank(), panel.grid.minor=element_blank()) +
  theme(axis.line=element_line(colour="#8f8f8f")) +
# theme(legend.position=c(0.13,0.89),
#       legend.background = element_rect(colour="#606060",fill="#FFFFFF",
#                                        size=.3,linetype='solid'),
#       axis.text=element_text(size=14),
#       axis.title=element_text(size=16),
#       plot.title=element_text(size=20)) +
  scale_fill_manual(values=c("#606060", "#DDDDDD"), name="") +
  ylab("Mean Normalized Transition Entropy") +
  xlab("TCQ (0) or TSQ (1)")  +
# ggtitle("Normalized Transition Entropy") +
  ylim(0,1)
dev.off()
# embedFonts(plotName, "pdfwrite", outfile = plotName,
#   fontpaths =
#   c("/opt/local/share/texmf-texlive/fonts/type1/urw/helvetic",
#     "/usr/share/texmf/fonts/type1/urw/helvetic",
#     "/usr/local/teTeX/share/texmf-dist/fonts/type1/urw/helvetic",
#     "/usr/share/texmf-texlive/fonts/type1/urw/helvetic",
#     "/usr/local/texlive/texmf-local/fonts/type1/urw/helvetic"))

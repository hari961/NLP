import sys
chunking = []
chunking_word = []
test_lines=[]
rules=['N_NN', 'PR_PRQ', 'RD_PUNC', 'N_NNPC RD_PUNC N_NNPC', 'QT_QTC N_NN RD_PUNC', 'QT_QTF N_NN', 'QT_QTF N_NN RD_PUNC', 'V_VM_VNF', 'V_VM_VF', 'PR_PRP', 'V_VN', 'DM_DMD N_NN PSP', 'PR_PRP QT_QTF', 'PR_PRP N_NN', 'RP_RPD QT_QTF N_NN', 'V_VM_VF RD_PUNC', 'PR_PRP N_NN RP_RPD', 'N_NN PSP RP_RPD', 'RB', 'PR_PRP RP_RPD', 'CC_CCS', 'V_VM_VF RP_RPD', 'CC_CCS_UT', 'N_NN PSP', 'JJ QT_QTF N_NN', 'DM_DMD N_NN', 'JJ QT_QTF N_NN RD_PUNC', 'PR_PRP PSP', 'PR_PRF N_NNC N_NNC RD_PUNC', 'N_NN RD_PUNC', 'V_VM_VINF', 'V_VN RD_PUNC', 'N_NN RP_RPD', 'N_NN N_NST RP_RPD', 'N_NN N_NST', 'QT_QTC N_NN', 'RD_PUNK', 'QT_QTC N_NN RP_RPD', 'V_VM_VNF RD_PUNC', 'QT_QTF QT_QTC N_NN', 'RP_RPD QT_QTF V_VM_VINF', 'RP_INTF QT_QTF N_NN', 'QT_QTC QT_QTF N_NN', 'V_VN N_NST', 'N_NNP', 'QT_QTF QT_QTF N_NN', 'QT_QTF QT_QTF N_NN PSP', 'JJ N_NN', 'CC_CCS RD_PUNC', 'RD_SYM RP_RPD N_NN', 'V_VM_VF RD_SYM', 'PR_PRF', 'RP_UNK', 'RP_RPD JJ N_NN', 'N_NNC N_NNC', 'V_VN PSP', 'V_VN RP_RPD', 'N_NN N_NST PSP RD_PUNC', 'V_VM_VNF RP_RPD', 'V_VM_VINF RD_PUNC', 'PR_PRP N_NN PSP', 'N_NNP RD_PUNC', 'N_NNP RP_RPD', 'JJ JJ N_NN', 'N_NNP PSP', 'RP_RPD N_NN', 'PR_PRF N_NN', 'RP_INTF N_NN RP_RPD', 'CC_CCD RD_PUNC', 'CC_CCS RP_RPD', 'PR_PRP N_NST RP_RPD', 'PR_PRC', 'PR_PRP N_NST', 'JJ N_NN PSP', 'QT_QTF N_NNC N_NNC', 'QT_QTF CC_CCD', 'PR_PRF N_NN N_NST', 'QT_QTF N_NN PSP', 'QT_QTF PR_PRQ RP_RPD', 'RP_INTF N_NN', 'QT_QTF N_NN RP_RPD', 'N_NNC N_NNC PSP', 'QT_QTF PR_PRP', 'V_VN PSP RP_RPD', 'N_NNC RD_SYM N_NNC N_NN', 'QT_QTF JJ N_NN', 'N_NNPC N_NNPC N_NNPC', 'N_NN RP_RPD PSP', 'RD_PUNC N_NN', 'N_NNPC N_NNPC RP_RPD', 'PR_PRP PR_PRP', 'V_VNV_VN', 'V_VM_VF RP_RPD RP_RPD RD_PUNC', 'CC_CCD', 'QT_QTF', 'V_VN PSP RD_PUNC', 'JJ QT_QTF N_NN RP_RPD', 'RP_UNK RD_PUNC', 'JJ N_NN RD_PUNC', 'JJ N_NN RP_RPD', 'JJ JJ N_NN RD_PUNC', 'PR_PRP N_NN RD_PUNC', 'PR_PRQ N_NN V_VM_VF RD_PUNCN_NN', 'QT_QTC QT_QTC N_NN', 'PR_PRF N_NN PSP', 'PR_PRF RP_INTF N_NN', 'PR_PRP PSP RP_RPD', 'QT_QTF JJ N_NN RD_PUNC', 'RP_RPD N_NNP RD_PUNC', 'N_NNC N_NNC RD_PUNC', 'N_NNC N_NNC RP_RPD', 'DM_DMD N_NN RP_RPD', 'QT_QTC N_NN N_NST', 'N_NN RP_RPD RD_PUNC', 'JJ RP_RPD N_NN', 'QT_QTO N_NN', 'QT_QTF N_NNC JJ N_NNC', 'CC_CCS_UT RP_RPD', 'RP_RPD V_VM_VF RD_PUNC', 'V_VM_VF PSP', 'PR_PRP JJ N_NN', 'DM_DMD JJ N_NN', 'QT_QTF N_NN N_NST', 'QT_QTF V_VN N_NST RP_RPD', 'QT_QTO N_NNC N_NNC', 'QT_QTC N_NNC N_NNC', 'N_NNPC N_NNPC RD_PUNC', 'N_NNPC N_NNPC', 'QT_QTC N_NN PSP', 'RP_RPD RB', 'QT_QTC', 'RB RD_PUNC', 'V_VM_VINF PSP', 'PR_PRP N_NNQT_QTF N_NN', 'RP_INTF JJ N_NN']
def return_tag(tag):
    temp=tag.split(" ")
    returntag=temp[0]
    for i in range(1,len(temp)-1):
        returntag += " "+temp[i]
    return returntag
if(len(sys.argv) != 2):
	print "Error : Give proper filename as input !"
	exit(0)
f=open(sys.argv[1])
lines=f.readlines()
for line in lines:
    try:
        temp=line[:-1]
        temp=temp.split(" ")
        test_lines.append(temp)
        build_chunk=""
        build_word=""
        chunking1=[]
        chunking2=[]
        for i in range(len(temp)):
            word_tag=temp[i].split("*")
            word=word_tag[0]
            tag=word_tag[1]
            if(build_chunk==""):
                build_chunk = tag
                build_word = word
            else:
                build_chunk += " " + tag
                build_word += " " + word

            if(build_chunk not in rules):
                if(len(build_chunk.split(" ")) > 1):
                    prev_tag=return_tag(build_chunk)
                    prev_word = return_tag(build_word)
                    build_chunk = tag
                    build_word = word
                else:
                    prev_tag=tag
                    prev_word = word
                    build_chunk = ""
                    build_word = ""
                chunking1.append(prev_tag)
                chunking2.append(prev_word)


        chunking1.append(build_chunk)

        chunking2.append(build_word)
        chunking.append(chunking1)
        chunking_word.append(chunking2)
    except:
        continue

for i in range(len(chunking_word)):
    for j in chunking_word[i]:
        print "[" + j + "]",


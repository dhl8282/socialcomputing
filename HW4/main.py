import blog
import nltk
import reuter

#HW1
#reuterCorpus = reuter.getReuter50Data()
#reuter.searchReuter50(reuterCorpus, ['Hong', 'Kong'])
#reuter.searchReuter50(reuterCorpus, ['technology'])
#reuter.searchReuter50(reuterCorpus, ['government'])
#reuter.searchReuter50(reuterCorpus, ['human', 'right'])

#HW2
blogCorpus = blog.getFeedContents()
td_matrix = reuter.getTDMatrix(blogCorpus)
reuter.getDoc(td_matrix)

#HW3
#reuterFirstArticles = reuter.getReuter50FirstArticle()
#td_matrix = reuter.getTDMatrix(reuterFirstArticles)
#reuter.getDoc(td_matrix)
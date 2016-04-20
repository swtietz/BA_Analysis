import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.cm
from scipy.signal.windows import gaussian
import sklearn.metrics
from DataSet import createDataSetFromFile

def createTargetShapeDelayFigure():
    gestureLen = 20
    gestureSig = np.concatenate([np.zeros((10,3)),np.random.normal(size=(gestureLen,3)),np.zeros((10,3))],0)
    target = np.concatenate([np.zeros((10,1)),np.ones((gestureLen,1)),np.zeros((10,1))],0)
    target_gaus = np.concatenate([np.zeros((5,1)),np.atleast_2d(gaussian(gestureLen+10,5)).T,np.zeros((5,1))],0)
    target_delayed = np.concatenate([np.zeros((28,1)),np.ones((5,1)),np.zeros((7,1))],0)
    
    fig, ax = plt.subplots(1, 3, sharey=True, sharex=True, figsize=(20,5))
    plt.ylim(-5,5)
    for axn in ax: 
        axn.plot(gestureSig,label='input signal')
        axn.plot([0,40],[0,0],c='black',linewidth=1)
    ax[0].plot(target,label='target',c='red',linewidth=2)
    ax[0].fill_between(np.arange(0,40),0,target.squeeze(),facecolor='red',alpha=0.5)
    ax[0].set_title('(a)')
    ax[1].plot(target_gaus,label='target',c='red',linewidth=2)
    ax[1].fill_between(np.arange(0,40),0,target_gaus.squeeze(),facecolor='red',alpha=0.5)
    ax[1].set_title('(b)')
    ax[2].plot(target_delayed,label='target',c='red',linewidth=2)
    ax[2].fill_between(np.arange(0,40),0,target_delayed.squeeze(),facecolor='red',alpha=0.5)
    ax[2].set_title('(c)')
    #plt.legend(bbox_to_anchor=(1., 1.05), loc=1, borderaxespad=0.)
    plt.tight_layout()
    projectPath = 'C:\Users\Steve\Documents\Uni\BAThesis\\src\\targetShapeDelay2.pdf'
    pp = PdfPages(projectPath)
    pp.savefig()
    pp.close()




def createEvaluationProblem():
    gestureLen = 20
    target = np.concatenate([np.ones((gestureLen,1)),np.zeros((10,1)),np.ones((gestureLen,1)),np.zeros((40,1))],0)
    target2 = np.concatenate([np.zeros((70,1)),np.ones((gestureLen,1))],0)
    pred1 = np.concatenate([np.ones((8,1)),np.zeros((5,1)),np.ones((8,1)),np.zeros((69,1))],0)
    pred2 = np.concatenate([np.zeros((7,1)),np.ones((7,1)),np.zeros((66,1)),np.ones((10,1))],0)
    zero = np.zeros((100,1))
    plt.figure(figsize=(20,5))
    #plt.plot(target, label='Target Gesture 1', color='red', linewidth=2, linestyle='--')
    #plt.plot(pred1, label='Pred. Gesture 1', color='red', linewidth=2, linestyle='-')
    #plt.plot(pred2, label='Pred. Gesture 2', color='blue', linewidth=2, linestyle='-')
    #plt.fill_between(np.arange(0,70), 0, 1, label='Target Gesture 1', facecolor='red', alpha=0.2, where=np.squeeze(target>0))
    #plt.fill_between(np.arange(0,70), 0, np.squeeze(pred1), label='Pred. Gesture 1', facecolor='red', where=np.squeeze(pred1>=pred2))
    #plt.fill_between(np.arange(0,70), 0, np.squeeze(pred2), label='Pred. Gesture 2', facecolor='blue', where=np.squeeze(pred2>=pred1))
    
    plt.plot(np.ones((90,1))*0.5,color='black')
    plt.plot(np.ones((90,1))*1,color='black')
    plt.plot(np.ones((90,1))*-0.5,color='black')
    plt.plot(np.ones((90,1))*-1,color='black')
    
    
    plt.fill_between(np.arange(0,90), 0.5, 1, label='no gesture', facecolor='grey', alpha=0.4)
    plt.fill_between(np.arange(0,90), 0.5, 1, facecolor='red', alpha=0.8, where=np.squeeze(target>0))
    plt.fill_between(np.arange(0,90), 0.5, 1, facecolor='blue', alpha=0.8, where=np.squeeze(target2>0))
    
    
    plt.fill_between(np.arange(0,90), -0.5, -1, facecolor='grey', alpha=0.4)
    plt.fill_between(np.arange(0,90), -0.5, -1, label='Gesture 1', facecolor='red', where=np.squeeze(pred1==1))
    plt.fill_between(np.arange(0,90), -0.50, -1, label='Gesture 2', facecolor='blue', where=np.squeeze(pred2==1))
    
    
    plt.fill_between(np.arange(0,90), -0.2, 0.2, facecolor='yellow', alpha=0.2)
    
    plt.annotate('TP',xy=(3.5,-0.1))
    plt.plot([3,10],[-0.75,0.75],linewidth=3, color='black')
    
    plt.annotate('WG',xy=(8,-0.1))
    plt.plot([10,10],[-0.75,0.75],linewidth=3, color='black')
    
    plt.annotate('FP',xy=(14,-0.1))
    plt.plot([17,10],[-0.75,0.75],linewidth=3, color='black')
    
    plt.annotate('TP',xy=(25,-0.1))
    plt.plot([30,25],[-0.75,0.75],linewidth=3, color='black')
    
    
    plt.annotate('FN',xy=(37,-0.1))
    plt.plot([40,40],[-0.75,0.75],linewidth=3, color='black')
    
    plt.annotate('TP',xy=(57.5,-0.1))
    plt.plot([60,60],[-0.75,0.75],linewidth=3, color='black')
    
    plt.annotate('TP',xy=(83.5,-0.1))
    plt.plot([85,80],[-0.75,0.75],linewidth=3, color='black')
    
    
    
    plt.yticks([-0.75,0,0.75])
    plt.setp(plt.gca(), 'yticklabels', ['Prediction','Mapping','Target'])
    
    plt.ylim(-1.5,1.5)
    plt.xlim(0,120)
    plt.legend()
    projectPath = 'C:\Users\Steve\Documents\Uni\BAThesis\\src\\classificationProb.pdf'
    pp = PdfPages(projectPath)
    pp.savefig()
    pp.close()


    true = [1,1,1,2,3,3,3]
    pred = [1,2,3,2,1,3,3]
    print sklearn.metrics.f1_score(true,pred,average=None)
    print np.mean(sklearn.metrics.f1_score(true,pred,average=None))
    
    
    
    
def createInputSignalFigure():
    errors = [0.272813277233,0.233033147087,0.217966453407,0.139282580674,0.0953774246893,0.0898370698925,0.0551168200035]
    labels = ['F','G','A','FG','FA','GA','FGA']
    
    ax = plt.subplot()
    #ax.bar(np.arange(0,7), errors, alpha=0.5)
    cmap = matplotlib.cm.brg_r
    for i, error in enumerate(errors):
        ax.bar([i], errors[i], facecolor=cmap(error/0.5), alpha=1)
    
    ax.set_xticks(np.arange(0.5,7.5,1))
    ax.set_xticklabels(labels)
    plt.ylabel('Validation Error')
    plt.xlabel('Input signal')
    plt.xlim(-0.5,7.5)
    plt.ylim(0,0.5)
    projectPath = 'C:\Users\Steve\Documents\Uni\BAThesis\\src\\errorByInput.pdf'
    pp = PdfPages(projectPath)
    pp.savefig()
    pp.close()
    return ax


def createGroundTruthCreation():
    ds = createDataSetFromFile('julian_0_fullSet.npz')
    


if __name__ == '__main__':
    matplotlib.rcParams.update({'font.size': 20})
    createGroundTruthCreation()


    
    
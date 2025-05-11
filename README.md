# Automated Originality Assessment of academic Paper: A Collaborative Approach Integrating Human Expertise and Large Language Models

## Overview

**Dataset and source code for paper "Automated Originality Assessment of academic Paper: A Collaborative Approach Integrating Human Expertise and Large Language Models".**

This study introduces a novel method for evaluating the originality and decision-making processes of academic articles by leveraging peer reviews and the methodology sections of scholarly papers. The primary contributions of this paper include:

- Proposing a new method for predicting the originality and decision-making of academic articles.
- Investigating a new method to combine human and artificial intelligence knowledge to enhance the performance of deep learning models.
- Designing a text-guided fusion module to integrate human and artificial intelligence knowledge effectively, facilitating optimal utilization of both sources of information.
- Conducting comprehensive experiments demonstrating the effectiveness of our methodology, which has yielded commendable results.

## Model overview

This study proposes a framework consisting of knowledge-guided fusion module.<br>
![image](https://github.com/user-attachments/assets/6d469c02-a6e6-4c72-8a6d-23ea4e8cff91)


## Directory structure

<pre>
originality_predict                               Root directory
├── Code                                          Source code folder
│   ├── baseline_model                            Baseline model folder
│   │    ├── load_method.py                       Load data for Review and Method as input
│   │    ├── main.py                              Train the model for Review and Feedback as input
│   │    ├── method_main.py                       Train the model for Review and Method as input
│   │    ├── model.py                             Model structure
│   │    ├── predict.py                           Predict the result
│   │    ├── split_data.py                        Load data for Review and Feedback as input
│   │    ├── util.py                              Data process tool
│   ├── Bi_interaction.py                         Proposed model structure      
│   ├── p_predict.py                              Predict the result
│   └── proposed_main.py                          Train the proposed model 
│   └── read_data.py                              Load data for Review and Feedback
├── Dataset                                       Dataset folder
│   └── Dataset.json                              Preprocessed Dataset
│
└── README.md
</pre>
## Dataset Discription

The dataset contains four contents: 
  - "novelty_sentence": Originality evaluation sentences by reviewers
  - "chat_content"： Feedback from ChatGPT
  - "nov_score":  Technical Novelty And Significance score
  - "decision":  Paper decsion
  - A Sample From Dataset: 
{"id": "-0Cjhnl-dhK",
**"novelty_sentence"**: "Methodologically speaking, it is not clear to me what is the contribution of this paper.They propose a constrained optimization framework to achieve such results and demonstrate it empirically on different tasks.......which is a constrained optimization alternative to empirical risk minimization. Overall, I liked this paper.", 
**"chat_content"**: "The article \"TOWARDS UNCERTAINTIES IN DEEP LEARNING THAT ARE ACCURATE AND CALIBRATED\" presents a novel approach to achieving calibrated and sharp predictive uncertainties in machine learning models....... The article provides a detailed algorithm for achieving calibrated learning of probabilistic models and discusses the practical considerations and benefits of calibrated predictive uncertainties in machine learning applications.\n", "method_content": "Supervised machine learning models commonly predict a probability distribution over the output variables -e.g. class membership probabilities or the parameters of an exponential family distribution.........Efficient Exploration. Balancing exploration and exploitation is a common challenge in many applications on machine learning such as reinforcement learning, Bayesian optimization, and active learning. When probabilistic models are uncalibrated, inaccurate confidence intervals might incentivize the model to explore ineffective actions, degrading performance. Calibrated uncertainties have been shown to improve decision-making in bandits (Malik et al., 2019) and likely to extend to Bayesian optimization and active learning as well.Other Applications. The importance of accurate confidence estimates has been highlighted by practitioners in many fields, including medicine (Saria, 2018) , meteorology (Raftery et al., 2005) , and natural language processing (Nguyen and O'Connor, 2015) . Accurate confidence estimates also play an important in computer vision applications, such as depth estimation (Kendall and Gal, 2017) .", 
**"novelty_score"**: 2, 
**"decision"**: 1}
## Quick Start

<b> </b>
    - <code> python ./Code/baseline_model./method_main.py</code>  Execute this command to train model with Review and Method as input.<br>
    - <code> python ./Code/baseline_model./main.py</code>  Execute this command to train model with Review and Feedback as input.<br>
    - <code> python ./Code/proposed_main.py</code>  Execute this command to train our proposed model.<br>
## Main result
The results generated by the large language models in this paper can be found at https://drive.google.com/drive/folders/1acu1HKqts-fGFKkq0aVI8XXJgoKl4HBr?usp=drive_link
- <b>Results of originality prediction.</b><br>
<div align=center>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=184 rowspan=2 style='width:138.25pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><a
  name="_Hlk160115425"><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman",serif'>Models</span></a></p>
  </td>
  <td width=184 colspan=2 style='width:138.25pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Review &amp;
  method</span></p>
  </td>
  <td width=184 colspan=2 style='width:138.3pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Review &amp;
  feedback</span></p>
  </td>
 </tr>
 <tr>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>F1</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Accuracy</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>F1</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Accuracy</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>BERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.70</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.72</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.72</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>RoBERTa</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.68</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.67</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>SciBERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.70</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.73</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.74</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>XLNet</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.62</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.62</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.69</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>AlBERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.52</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.54</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.64</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.64</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours-BERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.81</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.82</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours- RoBERTa</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.78</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.79</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours- SciBERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.83</span></b></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.84</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours- XLNet</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.78</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.79</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours- AlBERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.76</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.77</span></p>
  </td>
 </tr>
</table>

</div>


## Case study

We conduct a case study for different input and our method.
![image](https://github.com/user-attachments/assets/024c293e-cdd9-4db3-ac63-61b663e2be2a)


## Dependency packages
System environment is set up according to the following configuration:
- transformers==4.16.2
- nltk==3.6.7
- matplotlib==3.5.1
- scikit-learn==1.1.3
- pytorch 2.0.1
- tqdm 4.65.0
- numpy 1.24.1

## Acknowledgement

We express our gratitude to the team at openreview.net for their dedication to advancing transparency and openness in scientific communication. We utilized the aspect identifying tool developed by Yuan et al.（2022）(https://github.com/neulab/ReviewAdvisor).

>Yuan, W., Liu, P., & Neubig, G. (2022). Can we automate scientific reviewing?. Journal of Artificial Intelligence Research, 75, 171-212.<br>


## Citation
Please cite the following paper if you use this code and dataset in your work.
    
>Wenqing Wu, Chengzhi Zhang\*, Yi Zhao. (2024). Automated Academic Paper Evaluation: A Collaborative Approach Integrating Human Expertise and Large Language Models. ***Journal of the Association for Information Science and Technology***.（submitted)  [[Dataset & Source Code]](https://github.com/njust-winchy/originality_predict/)) 

# RefTools

## CommonRefs

Have you ever looked at your library of references and wondered: Have I missed an important publication on the topic?  
Or, more specifically: What publications are most frequently cited in my references?

**commonrefs.py** answers the question by parsing the references in your BibTeX file, looking up which papers they cite, and generating a ranking of the cited papers.

### Dependencies

Install the required python packages via `pip3 install requests`

### Preparation

1. Get the Elsevier Developers&reg; API Key at https://dev.elsevier.com/user/login and save it inside *api_key.txt* in the repository folder.
2. Copy your library's **.bib* file into the repository folder. The BibTeX entries must contain the Document Object Identifiers (DOIs) in the `doi` field. Mendeley can automatically fetch DOIs.

### Usage
Open the command line in the repository folder and run `python3 commonrefs.py`.

### Output
Example:
```
Document ID (doi) found for 190 publications
No references found for 49 publications (see not_found.txt file)

Results:
29 x A model of saliency-based visual attention for rapid scene analysis    ?
24 x ImageNet classification with deep convolutional neural networks
21 x Learning to predict where humans look
20 x Very deep convolutional networks for large-scale image recognition
15 x Shifts in selective visual attention: Towards the underlying neural circuitry    ?
14 x The pascal visual object classes (VOC) challenge    x
14 x Graph-based visual saliency
12 x Saliency based on information maximization
12 x Contextual guidance of eye movements and attention in real-world scenes: The role of global features in object search
11 x Rich feature hierarchies for accurate object detection and semantic segmentation
10 x A feature-integration theory of attention
10 x Object detection with discriminatively trained part-based models
10 x A saliency-based search mechanism for overt and covert shifts of visual attention    ?
10 x State-of-the-art in visual attention modeling
9 x SUN: A Bayesian framework for saliency using natural statistics    ?
9 x Quantitative analysis of human-model agreement in visual saliency modeling: A comparative study
9 x Gradient-based learning applied to document recognition
9 x Modeling the role of salience in the allocation of overt visual attention    ?
9 x Computational modelling of visual attention    ?
9 x Histograms of oriented gradients for human detection    x
...
```

The number at the beginning of the file indicates the number of times this publication has been cited in the references.  
A `x` at the end of the line indicates that neither the title nor the DOI has been found in the BibTeX file.  
A `?` at the end of the line indicates that the title has not been found in the BibTeX file and no DOI could be retrieved.
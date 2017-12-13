# In short

- **url**: [https://nlesc.github.io/case-law-app/](https://nlesc.github.io/case-law-app/)
    - IP-whitelisting: No
    - Requires login: No
    - Works better with GPU: N/A
    - Database: N/A, the app contains about 240kB data
    - Network: Transferring data is not a bottleneck for this demo
- **screencast**: Not available
- **contact person**: [Dafne van Kuppevelt](https://www.esciencecenter.nl/profile/dafne-van-kuppevelt-msc)
- **screenshot**:
![screenshot](/demos/caselaw/screencapture-demo-caselaw.png "Caselaw Screenshot")

# General idea of the project

The law is a text that describes what a person or legal entity can and cannot
do. However, the law is somewhat open to interpretation. This interpretation is
done by judges whenever a case is brought to court. Over time, the outcome of
individual cases build what is called _case law_.

Because consistency is crucial for the fair application of the law, cases often
reference other cases: if the reasoning behind a ruling in one case also applies
to another case, then the ruling should be the same. To warrant consistency it
is thus paramount that any relevant rulings from previous cases are identified.
Conventionally, both the justice department and the defense depend on legal
experts to make this identification when preparing a case. However, court
rulings are often difficult to understand, there is only limited time available,
and even experts are not aware of all cases that may be relevant.

The aim of this project was therefore to develop software that could assist the
legal community at large (prosecutors, judges, lawyers, legal aids, but also
researchers and students) in analyzing case law. For this, NLeSC worked together
with Maastricht University to develop an interactive visualization. This has
been implemented as follows. The collective of cases that together make up case
law can be thought of as a network, or _graph_. Each node in the graph
represents a case, while the edges represent references to other cases. The
graph can be visualized to make it easy for a non-technical user to discover
which cases are related. By using metrics from graph theory, such as
_in-degree_, _out-degree_, _betweenness_, etc., the nodes in the graph can be
annotated with additional information. The additional  information helps a
researcher quickly assess a node's importance. By presenting case law visually
as a graph, the structure underpinning case law is made explicit.

# Demo usage

1. Go to https://nlesc.github.io/case-law-app/
1. Either use the data set that ships with the app, or load your own.
1. Play with the filtering to show or hide nodes with certain properties. E.g.
only show nodes that are from a certain _Rechtsgebied_ or nodes that are from a
certain _year_ range. Or filter based on _in-degree_ to see only those cases
which are referenced often.
1. At any time, click on a node to show the details about the associated court
decision.  Click on the link in the details pane to go to the online document at
https://uitspraken.rechtspraak.nl. Let the audience study the ruling for a bit,
to see how difficult it is to make sense of it. Imagine you have to remember the
relations between hundreds of such documents! Much better to have the app.

## About network metrics

| Term as used in GUI | meaning |
| :--- | :--- |
| *degree* | TODO |
| *in-degree* | number of incoming references, higher numbers represent more  important cases. |
| *out-degree* | number of outgoing references, higher numbers represent cases that are well grounded in existing case law |
| *year* | year in which the ruling was issued |
| *hubs* | hub-score, as determined by the HITS algorithm. Indicates how much a case is cited by cases that are _authorities_ |
| *authorities* | authority-score, as determined by the HITS algorithm. Indicates how much a case is cited by nodes that are _hubs_ |
| *betweenness_centrality* | A measure for how many shortest paths go through a given node. A large betweenness signifies that that node connects several subareas of the network |
| *closeness_centrality* | TODO |
| *count_annotation* | TODO |
| *rel_in_degree* | Basically the same as in-degree, but corrected for case age (since young cases haven't had the chance to get cited as much as older cases) |
| *pagerank* | Importance measure as determined by the PageRank algorithm |

## Known quirks

In general, the app behaves pretty predictable. Only exception is the _adjust
layout for slider_ checkbox and the slider right above it. Still, good job
Dafne!

# Scientifically interesting aspects

- Explore area of law (clusters, sub-areas)
- What cases are important in the network?
- Compare ruling behavior of judges with analyses in literature
- Inspiration for new research questions
- Testimonial by Gijs van Dijck, Professor of Private Law at Maastricht
University: “_One master student was discussing cases the other day with an
expert in the field, and after running a network analysis on the data set for a
few minutes, he could point out some cases that the expert had missed. It’s
quite amazing to see how, thanks to this tool, a student can, in some ways,
outperform the expert._”


# Technologically interesting aspects

- Application of graph theory to case law text

# Further reading

- Project [website](https://www.esciencecenter.nl/project/case-law-analytics) on
esciencecenter.nl
- Dafne's [lunch presentation](https://web.microsoftstream.com/video/0f839d2b-4ed8-482f-8efb-ebec5bd0a740)
about Case Law Analytics March 23, 2017 (bad audio; requires login)
- Dafne's [presentation](https://web.microsoftstream.com/video/af9aecd1-3e1e-496a-9c6e-015260995399)
about Case Law Analytics at the ASDI information event April 4, 2017 (bad audio; requires login)
- Ilya's [lunch presentation](https://web.microsoftstream.com/video/f9ed3dfd-2dd0-41af-8871-0d4f336f4cfe)
about Case Law Analytics June 29, 2017 (bad audio; requires login)
- blog [post](https://blog.esciencecenter.nl/how-can-network-analysis-lead-to-a-new-way-of-studying-court-decisions-686ccf4d46aa)
about how network analysis leads to a new way of studying court decisions
- YouTube [video](https://www.youtube.com/watch?v=pjkYtaaxnco) by Law Blogs
Maastricht
- SharePoint [folder](https://nlesc.sharepoint.com/sites/operations/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120001A213E64C8D7E54D8BFB41016C82CC80&id=%2Fsites%2Foperations%2FShared%20Documents%2FProjectportfolio%2FProjects%2F27016P05%20Case%20Law%20Analytics) (requires login)
- [paper](https://dx.doi.org/10.3233/978-1-61499-838-9-95)
_Answering Legal Research Questions About Dutch Case Law with Network Analysis
and Visualization_


```latex
\documentclass[11pt]{article}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{titlesec}

% Custom Title Section Formatting
\titleformat{\section}
  {\vspace{-10pt} \Large \bfseries \raggedright}
  {}
  {\vspace{5pt}}
  {\vspace{5pt}}

\begin{document}

\noindent
\begin{center}
    \Large Kaustav Chanda \\
    Senior Software Engineer
\end{center}

\noindent
\begin{tabular}[t]{c}
    (cid:131) 9748802973 \\
    kaustav.chanda.work@gmail.com \\
    /LinkedIn § /kstv364 \\
    /medium ˆ /Kaustav97
\end{tabular}

\vspace{0.5cm}

\section{Experience}

\textbf{Hyland Software} \hfill Oct 2024 – Present \\
Developer 2, Content Federation Services, Kolkata, West Bengal

\begin{itemize}[leftmargin=*, itemsep=0.2em]
    \item Developed a scalable WebSocket broker application to federate information exchange, leveraging a plugin-based architecture.
    \item Developed a test harness using API Gateway reducing endpoint validation time by 40%, enabling faster debugging and integration testing.
    \item Refactored the broker WebSocket application using Factory, Adapter, and Dependency Injection design patterns for improved maintainability and scalability.
    \item Implemented unit tests achieving >85\% test coverage, enhancing system reliability and reducing production bugs by 30\%.
    \item Designed and implemented a PoC for streaming large files (>20GB) between AWS S3 and on-prem servers, achieving seamless content federation with a 20\% improvement in transfer efficiency.
    \item Automated CI/CD pipelines using GitHub Actions, improving deployment frequency by 3x, integrating SonarCloud scanning, automated tests, and deployments to sandbox and staging environments.
\end{itemize}

\vspace{0.5cm}

\textbf{Hyland Software} \hfill Feb 2022 – Sep 2024 \\
Developer 2, Onbase Engineering, Kolkata, West Bengal

\begin{itemize}[leftmargin=*, itemsep=0.2em]
    \item Developed PDF Support feature for OnBase viewer, bringing native PDF functionalities, generating 3000+ customer interest points.
    \item Modernized development workflow using Typescript and Webpack, promoting test-driven-development.
    \item Containerized legacy web application and automated Docker image creation using Jenkins, reducing build setup time by around 75\%.
    \item Utilized Jenkins and Vagrant to automate VM provisioning, nightly builds, and testing, streamlining the CI/CD process.
    \item Resolved accessibility defects following WCAG guidelines, reducing accessibility backlog by 13\%.
\end{itemize}

\vspace{0.5cm}

\textbf{Hyland Software} \hfill Aug 2020 – Jan 2022 \\
Developer 1, Onbase Engineering, Kolkata, West Bengal

\begin{itemize}[leftmargin=*, itemsep=0.2em]
    \item Contributed to the development of Hyland’s modern Angular platform for OnBase, integrating GraphQL and REST endpoints.
    \item Developed a pre-import web-viewer module for document preview and manipulation.
    \item Integrated native desktop functionalities (scanning and printing) through a virtual print driver.
    \item Wrote UI automation and Unit tests using Protractor, Jest, Selenium, and increased code coverage to 73\%.
\end{itemize}

\vspace{0.5cm}

\section{Technical Skills}

\begin{itemize}[leftmargin=*, itemsep=0.2em]
    \item \textbf{Languages:} C#, HTML/CSS, Typescript, JavaScript, SQL
    \item \textbf{Developer Tools:} VS Code, Visual Studio, IntelliJ, Git, TFS
    \item \textbf{Technologies/Frameworks:} .NET, Linux, Jenkins, Docker, Webpack, Github Actions, AzureML, AWS SageMaker, Databricks, MLFlow
\end{itemize}

\vspace{0.5cm}

\section{Education}

Heritage Institute of Technology (DGPA - 8.95) July 2016 – May 2020 \\
Bachelor of Technology in Computer Science and Engineering, Kolkata, West Bengal

\vspace{0.5cm}

\section{Achievements}

\begin{itemize}[leftmargin=*, itemsep=0.2em]
    \item Hyland SPOT Award 2021, 2023
    \item NASA Space Apps Challenge 2017 Finalist
    \item School Topper in Mathematics
\end{itemize}

\end{document}
```
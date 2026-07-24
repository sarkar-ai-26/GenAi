from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from langchain_ollama.chat_models import ChatOllama
from langchain_classic.vectorstores import FAISS

embed = OllamaEmbeddings(model='embeddinggemma')
Model = ChatOllama(model='llama3.1:8b',temperature=0.5)

dataset = [
    Document(
        page_content="Generative AI is significantly accelerating the software development lifecycle (SDLC) through intelligent code completion, automated unit test generation, and autonomous bug remediation. Development teams using LLM-based coding assistants report up to 55% faster feature delivery. In DevOps, agentic GenAI workflows parse deployment logs, analyze system failure reports, and autonomously execute self-healing scripts within CI/CD pipelines. This reduces manual troubleshooting overhead by over 40% and mitigates critical integration defects prior to software releases.",
        metadata={
            "doc_id": "DOC-001",
            "title": "Generative AI in Software Development and DevOps Automation",
            "industry": "IT & Software Engineering",
            "tags": ["Software", "DevOps", "Code Generation", "CI/CD", "Automation"]
        }
    ),
    Document(
        page_content="In the automotive and manufacturing sectors, Generative AI transforms traditional telemetry into actionable root-cause narratives. Rather than simply flagging sensor anomalies, LLM-backed diagnostic tools ingest sensor logs and equipment manuals to explain exact failure mechanisms and recommend repair steps in plain language. This has reduced unplanned shop floor downtime by 30% to 35%. Additionally, generative models synthesize rare failure-mode data to train automated visual inspection systems, improving quality control pass rates and speeding up electronic control unit (ECU) testing workflows.",
        metadata={
            "doc_id": "DOC-002",
            "title": "Predictive Maintenance and Generative Quality Control in Manufacturing & Automotive",
            "industry": "Automotive & Manufacturing",
            "tags": ["Automotive", "Manufacturing", "Predictive Maintenance", "Quality Assurance", "IoT"]
        }
    ),
    Document(
        page_content="Generative AI addresses major operational bottlenecks in healthcare, particularly through ambient clinical documentation and accelerated pharmaceutical research. Ambient AI tools listen to patient-physician dialogue and automatically generate structured, EHR-ready clinical notes, cutting physician charting time by up to 2 to 3 hours daily. In pharmaceutical research, generative molecular design tools generate novel protein structures and predict bio-activity, compressing early-stage drug candidate discovery from years to months.",
        metadata={
            "doc_id": "DOC-003",
            "title": "Ambient Documentation and Accelerating Drug Discovery in Healthcare",
            "industry": "Healthcare & Life Sciences",
            "tags": ["Healthcare", "Clinical EHR", "Drug Discovery", "Pharma", "Ambient AI"]
        }
    ),
    Document(
        page_content="Financial institutions leverage Generative AI to automate narrative generation for quarterly earnings, compliance reports, and regulatory filings directly from structured ledger data. In fraud prevention, LLMs generate realistic synthetic transaction data to train deep learning fraud detection models without exposing real customer financial records or compromising PII regulations. This synthetic data training has enhanced real-time fraud detection accuracy against deepfake and social engineering attacks while lowering compliance review overhead.",
        metadata={
            "doc_id": "DOC-004",
            "title": "Automated Financial Reporting, Fraud Synthetic Data, and Risk Assessment",
            "industry": "Financial Services & Banking",
            "tags": ["Finance", "Banking", "Fraud Detection", "Financial Reporting", "Risk Analysis"]
        }
    ),
    Document(
        page_content="Generative AI has redefined customer experience by transitioning static chatbots into fully autonomous support agents. These agents resolve multi-step customer inquiries, handle order modifications, and synthesize personalized styling advice using Retrieval-Augmented Generation (RAG) over product catalogs. Enterprise support teams report 50% to 70% faster resolution times and a 14% increase in successful resolutions per hour. Furthermore, generative visual models enable virtual try-on features, cutting e-commerce return rates by 15% to 30%.",
        metadata={
            "doc_id": "DOC-005",
            "title": "Conversational Agentic Support and Hyper-Personalization in Retail",
            "industry": "Retail & Customer Support",
            "tags": ["Retail", "Customer Service", "E-Commerce", "Agentic Chatbots", "Virtual Try-On"]
        }
    ),
    Document(
        page_content="Large-scale logistics and hardware enterprises use RAG pipelines and vector databases to index thousands of technical specification documents, build manuals, and rack schematics. Field engineers query real-time equipment health, inventory levels, and assembly procedures using conversational natural language interfaces. Replacing manual technical document searching with RAG-based search cuts document review times by up to 60%, drastically accelerating maintenance cycles and cross-border hardware flashing routines.",
        metadata={
            "doc_id": "DOC-006",
            "title": "Enterprise Search and RAG for Global Asset and Inventory Management",
            "industry": "Logistics & Hardware Engineering",
            "tags": ["Logistics", "RAG", "Asset Management", "Knowledge Management", "Vector Search"]
        }
    )
]

Query = 'How is GenAi helping the tech industry?'

vector_store = FAISS.from_documents(dataset,embed)

base_Retriever = vector_store.as_retriever()

compressor = LLMChainExtractor.from_llm(Model)

compression_retrieval = ContextualCompressionRetriever(base_compressor=compressor,base_retriever=base_Retriever)

result = compression_retrieval.invoke(Query)

for i in result:
    print(i, i.page_content)

from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

# PDF Directory (current directory)
PDF_DIR = os.path.dirname(os.path.abspath(__file__))

# Predefined Sets
sets_data = {
    'set1': {
        'name': 'Set 1: Basic Concepts & Architecture',
        'description': 'Foundational 5G concepts, network architecture, and technical reference guides.',
        'pdfs': [
            '5G_Concepts_Guide1.pdf',
            '5G_Core_Concepts.pdf',
            '5G_Core_Network_Architecture.pdf',
            '5G_Complete_Technical_Reference.pdf',
            '5G_Telecom_Reference_Guide.pdf',
            '5G_Call_Flow_Diagrams.pdf'
        ]
    },
    'set2': {
        'name': 'Set 2: Policies, Subscriptions & IDs',
        'description': 'Deep dive into 5G policies, SUPI/SUCI formats, and usage types.',
        'pdfs': [
            '5g_SUPI_NAI.pdf',
            '5G_SUCI_NAI_SUPI.pdf',
            '5G_Policy_Authorization.pdf',
            '5G_policy.pdf',
            'UE_Usage_Type_5G.pdf',
            '5g_roaming_scenarios.pdf'
        ]
    },
    'set3': {
        'name': 'Set 3: Specific NFs & Interfaces',
        'description': 'Details regarding UDM, UDR, AUSF, EIR, and PFCP interfaces.',
        'pdfs': [
            'UDM_5G_Complete_Guide.pdf',
            'UDM.pdf',
            '5G_UDM_UDR_Reference.pdf',
            '5G_Auth_Failure_AUSF_UDM.pdf',
            '5G_EIR_Reference.pdf',
            'PFCP_Session_IEs.pdf'
        ]
    },
    'set4': {
        'name': 'Set 4: Docker & Kubernetes',
        'description': 'Essential containerization and orchestration interview materials.',
        'pdfs': [
            'Docker and  K8s/Docker_Kubernetes_Interview_QA.pdf',
            'Docker and  K8s/docker-commands-guide_1.pdf',
            'Docker and  K8s/docker_tutorial.pdf',
            'Docker and  K8s/kubectl_k8s_notes.pdf',
            'Docker and  K8s/kubectl_k8s_notes1.pdf'
        ]
    },
    'set5': {
        'name': 'Set 5: Robot Framework',
        'description': 'QA and automation testing interview questions for Robot Framework.',
        'pdfs': [
            'Robot/Robot_Framework_100_Interview_QA.pdf'
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', sets=sets_data)

@app.route('/set/<set_id>')
def view_set(set_id):
    if set_id not in sets_data:
        abort(404)
    return render_template('set.html', set_id=set_id, set_info=sets_data[set_id])

@app.route('/pdf/<path:filename>')
def serve_pdf(filename):
    return send_from_directory(PDF_DIR, filename)

if __name__ == '__main__':
    # Use environment port for production (Render)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

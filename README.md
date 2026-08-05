# Resume Skill Parser API

A lightweight FastAPI service that scans resume text or candidate bios against common tech stack keywords. It calculates a simple match score and lists missing skills based on the target role provided.

## Features
- **Data Validation:** Uses Pydantic schemas to validate incoming JSON payloads.
- **Async Endpoints:** Built using FastAPI's async route handlers.
- **Swagger Docs:** Built-in interactive documentation available directly at `/docs`.

## Project Layout

```text
├── main.py          # API endpoints and skill matching logic
├── schemas.py       # Pydantic request & response models
├── requirements.txt # Project dependencies
└── README.md
Tech StackLayerTechnologyLanguagePython 3.10+Web FrameworkFastAPIValidation LayerPydantic v2ASGI ServerUvicornDeployment TargetRender.comLocal SetupClone the repository:Bashgit clone https://github.com/dreamyusha/resume-skill-parser.git
cd resume-skill-parser
Set up a virtual environment:Bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:Bashpip install -r requirements.txt
Start the server:Bashuvicorn main:app --reload
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)API ReferenceGET /healthHealth check endpoint.Response:JSON{
  "status": "ok"
}
POST /analyzeAnalyzes document text against a target role and returns a keyword match report.Sample Request:JSON{
  "text": "Experienced backend engineer skilled in Python, FastAPI, Docker, and Git. Built REST APIs.",
  "target_role": "Backend Developer"
}
Sample Response:JSON{
  "match_score": 40,
  "found_keywords": ["Python", "FastAPI", "Docker", "Git"],
  "missing_keywords": ["SQL", "Pydantic", "REST", "AWS", "Kubernetes", "Linux"],
  "summary": "Found 4 out of 10 target skills for Backend Developer."
}

4. Scroll to the bottom and click **Commit changes...** > **Commit changes**.

---

### 2. Add Topics to Your Repo (Boosts Searchability)

1. Go back to your main repository page (`github.com/dreamyusha/resume-skill-parser`).
2. Look at the right sidebar under **About** and click the gear icon ⚙️ next to "About".
3. Under **Topics**, type and add these tags:
   `fastapi` `python` `pydantic` `rest-api` `backend` `resume-parser`
4. Click **Save changes**.

---

### 3. Pin it to Your Profile

1. Click your profile avatar at the top right -> **Your profile**.
2. Click **Customize your pins** (or **Pin**).
3. Check the box for **`resume-skill-parser`** so it shows up at the top of your main GitHub profile page.

Once you deploy this repo on Render and drop your live link in the `About` section, your project link is ready 

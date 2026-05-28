import sys
import os
from dotenv import load_dotenv
from agent_core import BlankAgent

def load_brain_environment(brain_type):
    """선택한 두뇌에 맞는 env 파일을 찾아서 로드합니다."""
    env_file = f"{brain_type}.env"
    
    if not os.path.exists(env_file):
        print(f"[경고] {env_file} 파일이 없습니다! 템플릿 파일을 생성해 주세요.")
        sys.exit(1)
        
    load_dotenv(dotenv_path=env_file)
    print(f"[시스템] {env_file} 환경 변수 로드 완료")

def main():
    # 기본값은 gpt로 세팅 (예: python main.py gemini)
    brain_type = sys.argv[1].lower() if len(sys.argv) > 1 else "gpt"
    
    # 1. 에이전트 초기화 전, 선택한 두뇌의 환경변수만 먼저 로드
    load_brain_environment(brain_type)
    
    print("\n=== Blank Slate AI Agent CLI ===")
    
    # 2. 에이전트 생성 (이 시점엔 이미 필요한 키값이 os.environ에 들어있음)
    agent = BlankAgent(brain_type=brain_type)
    
    while True:
        try:
            user_input = input("\nAgent> ")
            if user_input.strip().lower() in ['exit', 'quit']:
                print("에이전트를 종료합니다.")
                break
            if not user_input.strip():
                continue
                
            response = agent.process_command(user_input)
            print(f"\n> {response}")
            
        except KeyboardInterrupt:
            print("\n에이전트를 강제 종료합니다.")
            break

if __name__ == "__main__":
    main()
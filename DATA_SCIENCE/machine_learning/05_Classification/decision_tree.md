# 결정 트리
> 머신러닝 알고리즘 중 가장 직관적인 알고리즘이다. 데이터에 있는 규칙을 학습을 통해 자동으로 찾아내고 트리 기반의 분류 규칙을 만드는 알고리즘이다.
> ![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQS9NpfijRlMMq_AjadZRt4L7N2M50GfrwqkmlkCubvnZA9d553JJl0zpsnXnsokcY45hg&usqp=CAU)
> - 의사결정 나무
>   - 규칙이 너무 많아지면 과적합이 발생한다. (결정 트리의 depth가 깊어질수록 예측 성능이 떨어진다.)
>   - 분류 나무
>   - 회귀 나무
> - **균일도**: 데이터가 얼마나 일관되고 유사한지 나타내는 지표이며 불순도라고도 표현한다.
> - **혼잡도(엔트로피)**: 얼마나 다양한 값 또는 패턴이 혼재되어 있는지를 나타내는 지표이다.
> - 정보 균일도가 높고 혼잡도가 낮은 데이터를 우선 선택해야 한다.
> ![](https://github.com/museonghwang/museonghwang.github.io/assets/77891754/3fe2079c-af5b-4a1d-8029-39c0b65eee0e)
> - 위의 이미지에서 A는 균일도가 높고 혼잡도도 높다.
> - C는 균일도가 낮고 혼잡도도 낮다.
> - 따라서 B를 가장 먼저 선택하여야 한다.


## 결정 트리 생성 및 규제 (gini 계수 및 하이퍼파라미터)
1. 훈련, 테스트 데이터를 분류한다.
2. StandardSaler 표준화를 진행한다.
3. `from sklearn.tree import DecisionTreeClassifier`
4. `dt_cfg = DecisionTreeClassifier(random_state=42)`: 결정 트리 객체 생성
   - **하이퍼파라미터**
   - `max_depth`를 특정 값으로 지정하면 결정트리의 depth를 조정하여 더 간결하게 표현 할 수 있다.
   - `mean_samples_split`을 특정 값으로 지정하면 결정트리의 노드가 값 이하로 떨어지면 리프노드로 결정하고 더 이상 depth를 늘리지 않는다.
5. 학습데이터에 훈련시킨다.
6. `from sklearn.tree import plot_tree`
7. `plot_tree(dt_cfg, filled=True, feature_names = [a, b, c, d])`: 결정 트리를 시각화시킨다. (이 때, 색깔을 채우고 조건 피처들을 나열한다.)
8. **`feature_importances_` 피처 중요도**
   - `sns.barplot(X=dt_cfg.feature_importances_, y=iris.feature_names)`: 트리를 만드는 데 각 피처가 얼마나 중요하지를 나타낸다.
   - 특정 피처들이 눈에 띄게 중요도가 높으면 그 피처들만으로도 분류를 할 수 있다.

### gini 계수
> gini 계수는 불순도를 수치화한 값이다.
> 어느 한쪽 클래스에 샘플이 몰려 있으면 gini 계수는 0이다.
> ![](https://lucy-the-marketer.kr/wp-content/uploads/2020/12/gini-index-example-1.png)

### 정보 이득 지수(Information Gain)
> 분류를 통해 정보에 대해 얻은 이득이다.
> 전체 데이터에 대한 지니 계수(root node에서)에서 각 속성의 gini 계수를 뺀 값이 가장 큰 값이 정보 이득이 가장 높다.
> 결정트리에서 엔트로피를 구하고 어떤 노드를 선택하는 것이 옳은지 따져볼 때 기댓값으로 정보 이득이 가장 높은 값을 선택한다. 
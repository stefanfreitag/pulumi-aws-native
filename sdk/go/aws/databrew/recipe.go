// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databrew

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::DataBrew::Recipe.
type Recipe struct {
	pulumi.CustomResourceState

	// Description of the recipe
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Recipe name
	Name  pulumi.StringOutput   `pulumi:"name"`
	Steps RecipeStepArrayOutput `pulumi:"steps"`
	Tags  RecipeTagArrayOutput  `pulumi:"tags"`
}

// NewRecipe registers a new resource with the given unique name, arguments, and options.
func NewRecipe(ctx *pulumi.Context,
	name string, args *RecipeArgs, opts ...pulumi.ResourceOption) (*Recipe, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Steps == nil {
		return nil, errors.New("invalid value for required argument 'Steps'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
		"tags[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Recipe
	err := ctx.RegisterResource("aws-native:databrew:Recipe", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRecipe gets an existing Recipe resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRecipe(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RecipeState, opts ...pulumi.ResourceOption) (*Recipe, error) {
	var resource Recipe
	err := ctx.ReadResource("aws-native:databrew:Recipe", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Recipe resources.
type recipeState struct {
}

type RecipeState struct {
}

func (RecipeState) ElementType() reflect.Type {
	return reflect.TypeOf((*recipeState)(nil)).Elem()
}

type recipeArgs struct {
	// Description of the recipe
	Description *string `pulumi:"description"`
	// Recipe name
	Name  *string      `pulumi:"name"`
	Steps []RecipeStep `pulumi:"steps"`
	Tags  []RecipeTag  `pulumi:"tags"`
}

// The set of arguments for constructing a Recipe resource.
type RecipeArgs struct {
	// Description of the recipe
	Description pulumi.StringPtrInput
	// Recipe name
	Name  pulumi.StringPtrInput
	Steps RecipeStepArrayInput
	Tags  RecipeTagArrayInput
}

func (RecipeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*recipeArgs)(nil)).Elem()
}

type RecipeInput interface {
	pulumi.Input

	ToRecipeOutput() RecipeOutput
	ToRecipeOutputWithContext(ctx context.Context) RecipeOutput
}

func (*Recipe) ElementType() reflect.Type {
	return reflect.TypeOf((**Recipe)(nil)).Elem()
}

func (i *Recipe) ToRecipeOutput() RecipeOutput {
	return i.ToRecipeOutputWithContext(context.Background())
}

func (i *Recipe) ToRecipeOutputWithContext(ctx context.Context) RecipeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RecipeOutput)
}

func (i *Recipe) ToOutput(ctx context.Context) pulumix.Output[*Recipe] {
	return pulumix.Output[*Recipe]{
		OutputState: i.ToRecipeOutputWithContext(ctx).OutputState,
	}
}

type RecipeOutput struct{ *pulumi.OutputState }

func (RecipeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Recipe)(nil)).Elem()
}

func (o RecipeOutput) ToRecipeOutput() RecipeOutput {
	return o
}

func (o RecipeOutput) ToRecipeOutputWithContext(ctx context.Context) RecipeOutput {
	return o
}

func (o RecipeOutput) ToOutput(ctx context.Context) pulumix.Output[*Recipe] {
	return pulumix.Output[*Recipe]{
		OutputState: o.OutputState,
	}
}

// Description of the recipe
func (o RecipeOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Recipe) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Recipe name
func (o RecipeOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Recipe) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o RecipeOutput) Steps() RecipeStepArrayOutput {
	return o.ApplyT(func(v *Recipe) RecipeStepArrayOutput { return v.Steps }).(RecipeStepArrayOutput)
}

func (o RecipeOutput) Tags() RecipeTagArrayOutput {
	return o.ApplyT(func(v *Recipe) RecipeTagArrayOutput { return v.Tags }).(RecipeTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RecipeInput)(nil)).Elem(), &Recipe{})
	pulumi.RegisterOutputType(RecipeOutput{})
}

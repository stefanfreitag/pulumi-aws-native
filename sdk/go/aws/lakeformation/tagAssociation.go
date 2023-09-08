// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lakeformation

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// A resource schema representing a Lake Formation Tag Association. While tag associations are not explicit Lake Formation resources, this CloudFormation resource can be used to associate tags with Lake Formation entities.
type TagAssociation struct {
	pulumi.CustomResourceState

	// List of Lake Formation Tags to associate with the Lake Formation Resource
	LfTags TagAssociationLfTagPairArrayOutput `pulumi:"lfTags"`
	// Resource to tag with the Lake Formation Tags
	Resource TagAssociationResourceOutput `pulumi:"resource"`
	// Unique string identifying the resource. Used as primary identifier, which ideally should be a string
	ResourceIdentifier pulumi.StringOutput `pulumi:"resourceIdentifier"`
	// Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string
	TagsIdentifier pulumi.StringOutput `pulumi:"tagsIdentifier"`
}

// NewTagAssociation registers a new resource with the given unique name, arguments, and options.
func NewTagAssociation(ctx *pulumi.Context,
	name string, args *TagAssociationArgs, opts ...pulumi.ResourceOption) (*TagAssociation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.LfTags == nil {
		return nil, errors.New("invalid value for required argument 'LfTags'")
	}
	if args.Resource == nil {
		return nil, errors.New("invalid value for required argument 'Resource'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"lfTags[*]",
		"resource",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TagAssociation
	err := ctx.RegisterResource("aws-native:lakeformation:TagAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTagAssociation gets an existing TagAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTagAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TagAssociationState, opts ...pulumi.ResourceOption) (*TagAssociation, error) {
	var resource TagAssociation
	err := ctx.ReadResource("aws-native:lakeformation:TagAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TagAssociation resources.
type tagAssociationState struct {
}

type TagAssociationState struct {
}

func (TagAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*tagAssociationState)(nil)).Elem()
}

type tagAssociationArgs struct {
	// List of Lake Formation Tags to associate with the Lake Formation Resource
	LfTags []TagAssociationLfTagPair `pulumi:"lfTags"`
	// Resource to tag with the Lake Formation Tags
	Resource TagAssociationResource `pulumi:"resource"`
}

// The set of arguments for constructing a TagAssociation resource.
type TagAssociationArgs struct {
	// List of Lake Formation Tags to associate with the Lake Formation Resource
	LfTags TagAssociationLfTagPairArrayInput
	// Resource to tag with the Lake Formation Tags
	Resource TagAssociationResourceInput
}

func (TagAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tagAssociationArgs)(nil)).Elem()
}

type TagAssociationInput interface {
	pulumi.Input

	ToTagAssociationOutput() TagAssociationOutput
	ToTagAssociationOutputWithContext(ctx context.Context) TagAssociationOutput
}

func (*TagAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((**TagAssociation)(nil)).Elem()
}

func (i *TagAssociation) ToTagAssociationOutput() TagAssociationOutput {
	return i.ToTagAssociationOutputWithContext(context.Background())
}

func (i *TagAssociation) ToTagAssociationOutputWithContext(ctx context.Context) TagAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TagAssociationOutput)
}

func (i *TagAssociation) ToOutput(ctx context.Context) pulumix.Output[*TagAssociation] {
	return pulumix.Output[*TagAssociation]{
		OutputState: i.ToTagAssociationOutputWithContext(ctx).OutputState,
	}
}

type TagAssociationOutput struct{ *pulumi.OutputState }

func (TagAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TagAssociation)(nil)).Elem()
}

func (o TagAssociationOutput) ToTagAssociationOutput() TagAssociationOutput {
	return o
}

func (o TagAssociationOutput) ToTagAssociationOutputWithContext(ctx context.Context) TagAssociationOutput {
	return o
}

func (o TagAssociationOutput) ToOutput(ctx context.Context) pulumix.Output[*TagAssociation] {
	return pulumix.Output[*TagAssociation]{
		OutputState: o.OutputState,
	}
}

// List of Lake Formation Tags to associate with the Lake Formation Resource
func (o TagAssociationOutput) LfTags() TagAssociationLfTagPairArrayOutput {
	return o.ApplyT(func(v *TagAssociation) TagAssociationLfTagPairArrayOutput { return v.LfTags }).(TagAssociationLfTagPairArrayOutput)
}

// Resource to tag with the Lake Formation Tags
func (o TagAssociationOutput) Resource() TagAssociationResourceOutput {
	return o.ApplyT(func(v *TagAssociation) TagAssociationResourceOutput { return v.Resource }).(TagAssociationResourceOutput)
}

// Unique string identifying the resource. Used as primary identifier, which ideally should be a string
func (o TagAssociationOutput) ResourceIdentifier() pulumi.StringOutput {
	return o.ApplyT(func(v *TagAssociation) pulumi.StringOutput { return v.ResourceIdentifier }).(pulumi.StringOutput)
}

// Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string
func (o TagAssociationOutput) TagsIdentifier() pulumi.StringOutput {
	return o.ApplyT(func(v *TagAssociation) pulumi.StringOutput { return v.TagsIdentifier }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TagAssociationInput)(nil)).Elem(), &TagAssociation{})
	pulumi.RegisterOutputType(TagAssociationOutput{})
}

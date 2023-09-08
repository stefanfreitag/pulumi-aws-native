// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package waf

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::WAF::SizeConstraintSet
//
// Deprecated: SizeConstraintSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type SizeConstraintSet struct {
	pulumi.CustomResourceState

	Name            pulumi.StringOutput                        `pulumi:"name"`
	SizeConstraints SizeConstraintSetSizeConstraintArrayOutput `pulumi:"sizeConstraints"`
}

// NewSizeConstraintSet registers a new resource with the given unique name, arguments, and options.
func NewSizeConstraintSet(ctx *pulumi.Context,
	name string, args *SizeConstraintSetArgs, opts ...pulumi.ResourceOption) (*SizeConstraintSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SizeConstraints == nil {
		return nil, errors.New("invalid value for required argument 'SizeConstraints'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SizeConstraintSet
	err := ctx.RegisterResource("aws-native:waf:SizeConstraintSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSizeConstraintSet gets an existing SizeConstraintSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSizeConstraintSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SizeConstraintSetState, opts ...pulumi.ResourceOption) (*SizeConstraintSet, error) {
	var resource SizeConstraintSet
	err := ctx.ReadResource("aws-native:waf:SizeConstraintSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SizeConstraintSet resources.
type sizeConstraintSetState struct {
}

type SizeConstraintSetState struct {
}

func (SizeConstraintSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*sizeConstraintSetState)(nil)).Elem()
}

type sizeConstraintSetArgs struct {
	Name            *string                           `pulumi:"name"`
	SizeConstraints []SizeConstraintSetSizeConstraint `pulumi:"sizeConstraints"`
}

// The set of arguments for constructing a SizeConstraintSet resource.
type SizeConstraintSetArgs struct {
	Name            pulumi.StringPtrInput
	SizeConstraints SizeConstraintSetSizeConstraintArrayInput
}

func (SizeConstraintSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sizeConstraintSetArgs)(nil)).Elem()
}

type SizeConstraintSetInput interface {
	pulumi.Input

	ToSizeConstraintSetOutput() SizeConstraintSetOutput
	ToSizeConstraintSetOutputWithContext(ctx context.Context) SizeConstraintSetOutput
}

func (*SizeConstraintSet) ElementType() reflect.Type {
	return reflect.TypeOf((**SizeConstraintSet)(nil)).Elem()
}

func (i *SizeConstraintSet) ToSizeConstraintSetOutput() SizeConstraintSetOutput {
	return i.ToSizeConstraintSetOutputWithContext(context.Background())
}

func (i *SizeConstraintSet) ToSizeConstraintSetOutputWithContext(ctx context.Context) SizeConstraintSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SizeConstraintSetOutput)
}

func (i *SizeConstraintSet) ToOutput(ctx context.Context) pulumix.Output[*SizeConstraintSet] {
	return pulumix.Output[*SizeConstraintSet]{
		OutputState: i.ToSizeConstraintSetOutputWithContext(ctx).OutputState,
	}
}

type SizeConstraintSetOutput struct{ *pulumi.OutputState }

func (SizeConstraintSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SizeConstraintSet)(nil)).Elem()
}

func (o SizeConstraintSetOutput) ToSizeConstraintSetOutput() SizeConstraintSetOutput {
	return o
}

func (o SizeConstraintSetOutput) ToSizeConstraintSetOutputWithContext(ctx context.Context) SizeConstraintSetOutput {
	return o
}

func (o SizeConstraintSetOutput) ToOutput(ctx context.Context) pulumix.Output[*SizeConstraintSet] {
	return pulumix.Output[*SizeConstraintSet]{
		OutputState: o.OutputState,
	}
}

func (o SizeConstraintSetOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *SizeConstraintSet) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o SizeConstraintSetOutput) SizeConstraints() SizeConstraintSetSizeConstraintArrayOutput {
	return o.ApplyT(func(v *SizeConstraintSet) SizeConstraintSetSizeConstraintArrayOutput { return v.SizeConstraints }).(SizeConstraintSetSizeConstraintArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SizeConstraintSetInput)(nil)).Elem(), &SizeConstraintSet{})
	pulumi.RegisterOutputType(SizeConstraintSetOutput{})
}

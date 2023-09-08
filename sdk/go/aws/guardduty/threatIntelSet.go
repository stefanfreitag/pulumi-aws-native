// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package guardduty

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::GuardDuty::ThreatIntelSet
//
// Deprecated: ThreatIntelSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ThreatIntelSet struct {
	pulumi.CustomResourceState

	Activate   pulumi.BoolOutput            `pulumi:"activate"`
	DetectorId pulumi.StringOutput          `pulumi:"detectorId"`
	Format     pulumi.StringOutput          `pulumi:"format"`
	Location   pulumi.StringOutput          `pulumi:"location"`
	Name       pulumi.StringPtrOutput       `pulumi:"name"`
	Tags       ThreatIntelSetTagArrayOutput `pulumi:"tags"`
}

// NewThreatIntelSet registers a new resource with the given unique name, arguments, and options.
func NewThreatIntelSet(ctx *pulumi.Context,
	name string, args *ThreatIntelSetArgs, opts ...pulumi.ResourceOption) (*ThreatIntelSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Activate == nil {
		return nil, errors.New("invalid value for required argument 'Activate'")
	}
	if args.DetectorId == nil {
		return nil, errors.New("invalid value for required argument 'DetectorId'")
	}
	if args.Format == nil {
		return nil, errors.New("invalid value for required argument 'Format'")
	}
	if args.Location == nil {
		return nil, errors.New("invalid value for required argument 'Location'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"detectorId",
		"format",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ThreatIntelSet
	err := ctx.RegisterResource("aws-native:guardduty:ThreatIntelSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetThreatIntelSet gets an existing ThreatIntelSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetThreatIntelSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ThreatIntelSetState, opts ...pulumi.ResourceOption) (*ThreatIntelSet, error) {
	var resource ThreatIntelSet
	err := ctx.ReadResource("aws-native:guardduty:ThreatIntelSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ThreatIntelSet resources.
type threatIntelSetState struct {
}

type ThreatIntelSetState struct {
}

func (ThreatIntelSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*threatIntelSetState)(nil)).Elem()
}

type threatIntelSetArgs struct {
	Activate   bool                `pulumi:"activate"`
	DetectorId string              `pulumi:"detectorId"`
	Format     string              `pulumi:"format"`
	Location   string              `pulumi:"location"`
	Name       *string             `pulumi:"name"`
	Tags       []ThreatIntelSetTag `pulumi:"tags"`
}

// The set of arguments for constructing a ThreatIntelSet resource.
type ThreatIntelSetArgs struct {
	Activate   pulumi.BoolInput
	DetectorId pulumi.StringInput
	Format     pulumi.StringInput
	Location   pulumi.StringInput
	Name       pulumi.StringPtrInput
	Tags       ThreatIntelSetTagArrayInput
}

func (ThreatIntelSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*threatIntelSetArgs)(nil)).Elem()
}

type ThreatIntelSetInput interface {
	pulumi.Input

	ToThreatIntelSetOutput() ThreatIntelSetOutput
	ToThreatIntelSetOutputWithContext(ctx context.Context) ThreatIntelSetOutput
}

func (*ThreatIntelSet) ElementType() reflect.Type {
	return reflect.TypeOf((**ThreatIntelSet)(nil)).Elem()
}

func (i *ThreatIntelSet) ToThreatIntelSetOutput() ThreatIntelSetOutput {
	return i.ToThreatIntelSetOutputWithContext(context.Background())
}

func (i *ThreatIntelSet) ToThreatIntelSetOutputWithContext(ctx context.Context) ThreatIntelSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ThreatIntelSetOutput)
}

func (i *ThreatIntelSet) ToOutput(ctx context.Context) pulumix.Output[*ThreatIntelSet] {
	return pulumix.Output[*ThreatIntelSet]{
		OutputState: i.ToThreatIntelSetOutputWithContext(ctx).OutputState,
	}
}

type ThreatIntelSetOutput struct{ *pulumi.OutputState }

func (ThreatIntelSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ThreatIntelSet)(nil)).Elem()
}

func (o ThreatIntelSetOutput) ToThreatIntelSetOutput() ThreatIntelSetOutput {
	return o
}

func (o ThreatIntelSetOutput) ToThreatIntelSetOutputWithContext(ctx context.Context) ThreatIntelSetOutput {
	return o
}

func (o ThreatIntelSetOutput) ToOutput(ctx context.Context) pulumix.Output[*ThreatIntelSet] {
	return pulumix.Output[*ThreatIntelSet]{
		OutputState: o.OutputState,
	}
}

func (o ThreatIntelSetOutput) Activate() pulumi.BoolOutput {
	return o.ApplyT(func(v *ThreatIntelSet) pulumi.BoolOutput { return v.Activate }).(pulumi.BoolOutput)
}

func (o ThreatIntelSetOutput) DetectorId() pulumi.StringOutput {
	return o.ApplyT(func(v *ThreatIntelSet) pulumi.StringOutput { return v.DetectorId }).(pulumi.StringOutput)
}

func (o ThreatIntelSetOutput) Format() pulumi.StringOutput {
	return o.ApplyT(func(v *ThreatIntelSet) pulumi.StringOutput { return v.Format }).(pulumi.StringOutput)
}

func (o ThreatIntelSetOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *ThreatIntelSet) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

func (o ThreatIntelSetOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ThreatIntelSet) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o ThreatIntelSetOutput) Tags() ThreatIntelSetTagArrayOutput {
	return o.ApplyT(func(v *ThreatIntelSet) ThreatIntelSetTagArrayOutput { return v.Tags }).(ThreatIntelSetTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ThreatIntelSetInput)(nil)).Elem(), &ThreatIntelSet{})
	pulumi.RegisterOutputType(ThreatIntelSetOutput{})
}

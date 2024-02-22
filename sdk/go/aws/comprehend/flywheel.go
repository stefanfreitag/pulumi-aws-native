// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package comprehend

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::Comprehend::Flywheel resource creates an Amazon Comprehend Flywheel that enables customer to train their model.
type Flywheel struct {
	pulumi.CustomResourceState

	ActiveModelArn     pulumi.StringPtrOutput              `pulumi:"activeModelArn"`
	Arn                pulumi.StringOutput                 `pulumi:"arn"`
	DataAccessRoleArn  pulumi.StringOutput                 `pulumi:"dataAccessRoleArn"`
	DataLakeS3Uri      pulumi.StringOutput                 `pulumi:"dataLakeS3Uri"`
	DataSecurityConfig FlywheelDataSecurityConfigPtrOutput `pulumi:"dataSecurityConfig"`
	FlywheelName       pulumi.StringOutput                 `pulumi:"flywheelName"`
	ModelType          FlywheelModelTypePtrOutput          `pulumi:"modelType"`
	Tags               aws.TagArrayOutput                  `pulumi:"tags"`
	TaskConfig         FlywheelTaskConfigPtrOutput         `pulumi:"taskConfig"`
}

// NewFlywheel registers a new resource with the given unique name, arguments, and options.
func NewFlywheel(ctx *pulumi.Context,
	name string, args *FlywheelArgs, opts ...pulumi.ResourceOption) (*Flywheel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DataAccessRoleArn == nil {
		return nil, errors.New("invalid value for required argument 'DataAccessRoleArn'")
	}
	if args.DataLakeS3Uri == nil {
		return nil, errors.New("invalid value for required argument 'DataLakeS3Uri'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"dataLakeS3Uri",
		"flywheelName",
		"modelType",
		"taskConfig",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Flywheel
	err := ctx.RegisterResource("aws-native:comprehend:Flywheel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFlywheel gets an existing Flywheel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFlywheel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FlywheelState, opts ...pulumi.ResourceOption) (*Flywheel, error) {
	var resource Flywheel
	err := ctx.ReadResource("aws-native:comprehend:Flywheel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Flywheel resources.
type flywheelState struct {
}

type FlywheelState struct {
}

func (FlywheelState) ElementType() reflect.Type {
	return reflect.TypeOf((*flywheelState)(nil)).Elem()
}

type flywheelArgs struct {
	ActiveModelArn     *string                     `pulumi:"activeModelArn"`
	DataAccessRoleArn  string                      `pulumi:"dataAccessRoleArn"`
	DataLakeS3Uri      string                      `pulumi:"dataLakeS3Uri"`
	DataSecurityConfig *FlywheelDataSecurityConfig `pulumi:"dataSecurityConfig"`
	FlywheelName       *string                     `pulumi:"flywheelName"`
	ModelType          *FlywheelModelType          `pulumi:"modelType"`
	Tags               []aws.Tag                   `pulumi:"tags"`
	TaskConfig         *FlywheelTaskConfig         `pulumi:"taskConfig"`
}

// The set of arguments for constructing a Flywheel resource.
type FlywheelArgs struct {
	ActiveModelArn     pulumi.StringPtrInput
	DataAccessRoleArn  pulumi.StringInput
	DataLakeS3Uri      pulumi.StringInput
	DataSecurityConfig FlywheelDataSecurityConfigPtrInput
	FlywheelName       pulumi.StringPtrInput
	ModelType          FlywheelModelTypePtrInput
	Tags               aws.TagArrayInput
	TaskConfig         FlywheelTaskConfigPtrInput
}

func (FlywheelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*flywheelArgs)(nil)).Elem()
}

type FlywheelInput interface {
	pulumi.Input

	ToFlywheelOutput() FlywheelOutput
	ToFlywheelOutputWithContext(ctx context.Context) FlywheelOutput
}

func (*Flywheel) ElementType() reflect.Type {
	return reflect.TypeOf((**Flywheel)(nil)).Elem()
}

func (i *Flywheel) ToFlywheelOutput() FlywheelOutput {
	return i.ToFlywheelOutputWithContext(context.Background())
}

func (i *Flywheel) ToFlywheelOutputWithContext(ctx context.Context) FlywheelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FlywheelOutput)
}

type FlywheelOutput struct{ *pulumi.OutputState }

func (FlywheelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Flywheel)(nil)).Elem()
}

func (o FlywheelOutput) ToFlywheelOutput() FlywheelOutput {
	return o
}

func (o FlywheelOutput) ToFlywheelOutputWithContext(ctx context.Context) FlywheelOutput {
	return o
}

func (o FlywheelOutput) ActiveModelArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Flywheel) pulumi.StringPtrOutput { return v.ActiveModelArn }).(pulumi.StringPtrOutput)
}

func (o FlywheelOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Flywheel) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o FlywheelOutput) DataAccessRoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Flywheel) pulumi.StringOutput { return v.DataAccessRoleArn }).(pulumi.StringOutput)
}

func (o FlywheelOutput) DataLakeS3Uri() pulumi.StringOutput {
	return o.ApplyT(func(v *Flywheel) pulumi.StringOutput { return v.DataLakeS3Uri }).(pulumi.StringOutput)
}

func (o FlywheelOutput) DataSecurityConfig() FlywheelDataSecurityConfigPtrOutput {
	return o.ApplyT(func(v *Flywheel) FlywheelDataSecurityConfigPtrOutput { return v.DataSecurityConfig }).(FlywheelDataSecurityConfigPtrOutput)
}

func (o FlywheelOutput) FlywheelName() pulumi.StringOutput {
	return o.ApplyT(func(v *Flywheel) pulumi.StringOutput { return v.FlywheelName }).(pulumi.StringOutput)
}

func (o FlywheelOutput) ModelType() FlywheelModelTypePtrOutput {
	return o.ApplyT(func(v *Flywheel) FlywheelModelTypePtrOutput { return v.ModelType }).(FlywheelModelTypePtrOutput)
}

func (o FlywheelOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Flywheel) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func (o FlywheelOutput) TaskConfig() FlywheelTaskConfigPtrOutput {
	return o.ApplyT(func(v *Flywheel) FlywheelTaskConfigPtrOutput { return v.TaskConfig }).(FlywheelTaskConfigPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FlywheelInput)(nil)).Elem(), &Flywheel{})
	pulumi.RegisterOutputType(FlywheelOutput{})
}

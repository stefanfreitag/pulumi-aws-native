// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package stepfunctions

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for StateMachine
type StateMachine struct {
	pulumi.CustomResourceState

	Arn                     pulumi.StringOutput                          `pulumi:"arn"`
	Definition              StateMachineDefinitionPtrOutput              `pulumi:"definition"`
	DefinitionS3Location    StateMachineS3LocationPtrOutput              `pulumi:"definitionS3Location"`
	DefinitionString        pulumi.StringPtrOutput                       `pulumi:"definitionString"`
	DefinitionSubstitutions StateMachineDefinitionSubstitutionsPtrOutput `pulumi:"definitionSubstitutions"`
	LoggingConfiguration    StateMachineLoggingConfigurationPtrOutput    `pulumi:"loggingConfiguration"`
	Name                    pulumi.StringOutput                          `pulumi:"name"`
	RoleArn                 pulumi.StringOutput                          `pulumi:"roleArn"`
	StateMachineName        pulumi.StringPtrOutput                       `pulumi:"stateMachineName"`
	StateMachineRevisionId  pulumi.StringOutput                          `pulumi:"stateMachineRevisionId"`
	StateMachineType        StateMachineTypePtrOutput                    `pulumi:"stateMachineType"`
	Tags                    StateMachineTagsEntryArrayOutput             `pulumi:"tags"`
	TracingConfiguration    StateMachineTracingConfigurationPtrOutput    `pulumi:"tracingConfiguration"`
}

// NewStateMachine registers a new resource with the given unique name, arguments, and options.
func NewStateMachine(ctx *pulumi.Context,
	name string, args *StateMachineArgs, opts ...pulumi.ResourceOption) (*StateMachine, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"stateMachineName",
		"stateMachineType",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource StateMachine
	err := ctx.RegisterResource("aws-native:stepfunctions:StateMachine", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStateMachine gets an existing StateMachine resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStateMachine(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StateMachineState, opts ...pulumi.ResourceOption) (*StateMachine, error) {
	var resource StateMachine
	err := ctx.ReadResource("aws-native:stepfunctions:StateMachine", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StateMachine resources.
type stateMachineState struct {
}

type StateMachineState struct {
}

func (StateMachineState) ElementType() reflect.Type {
	return reflect.TypeOf((*stateMachineState)(nil)).Elem()
}

type stateMachineArgs struct {
	Definition              *StateMachineDefinition              `pulumi:"definition"`
	DefinitionS3Location    *StateMachineS3Location              `pulumi:"definitionS3Location"`
	DefinitionString        *string                              `pulumi:"definitionString"`
	DefinitionSubstitutions *StateMachineDefinitionSubstitutions `pulumi:"definitionSubstitutions"`
	LoggingConfiguration    *StateMachineLoggingConfiguration    `pulumi:"loggingConfiguration"`
	RoleArn                 string                               `pulumi:"roleArn"`
	StateMachineName        *string                              `pulumi:"stateMachineName"`
	StateMachineType        *StateMachineType                    `pulumi:"stateMachineType"`
	Tags                    []StateMachineTagsEntry              `pulumi:"tags"`
	TracingConfiguration    *StateMachineTracingConfiguration    `pulumi:"tracingConfiguration"`
}

// The set of arguments for constructing a StateMachine resource.
type StateMachineArgs struct {
	Definition              StateMachineDefinitionPtrInput
	DefinitionS3Location    StateMachineS3LocationPtrInput
	DefinitionString        pulumi.StringPtrInput
	DefinitionSubstitutions StateMachineDefinitionSubstitutionsPtrInput
	LoggingConfiguration    StateMachineLoggingConfigurationPtrInput
	RoleArn                 pulumi.StringInput
	StateMachineName        pulumi.StringPtrInput
	StateMachineType        StateMachineTypePtrInput
	Tags                    StateMachineTagsEntryArrayInput
	TracingConfiguration    StateMachineTracingConfigurationPtrInput
}

func (StateMachineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stateMachineArgs)(nil)).Elem()
}

type StateMachineInput interface {
	pulumi.Input

	ToStateMachineOutput() StateMachineOutput
	ToStateMachineOutputWithContext(ctx context.Context) StateMachineOutput
}

func (*StateMachine) ElementType() reflect.Type {
	return reflect.TypeOf((**StateMachine)(nil)).Elem()
}

func (i *StateMachine) ToStateMachineOutput() StateMachineOutput {
	return i.ToStateMachineOutputWithContext(context.Background())
}

func (i *StateMachine) ToStateMachineOutputWithContext(ctx context.Context) StateMachineOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StateMachineOutput)
}

func (i *StateMachine) ToOutput(ctx context.Context) pulumix.Output[*StateMachine] {
	return pulumix.Output[*StateMachine]{
		OutputState: i.ToStateMachineOutputWithContext(ctx).OutputState,
	}
}

type StateMachineOutput struct{ *pulumi.OutputState }

func (StateMachineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StateMachine)(nil)).Elem()
}

func (o StateMachineOutput) ToStateMachineOutput() StateMachineOutput {
	return o
}

func (o StateMachineOutput) ToStateMachineOutputWithContext(ctx context.Context) StateMachineOutput {
	return o
}

func (o StateMachineOutput) ToOutput(ctx context.Context) pulumix.Output[*StateMachine] {
	return pulumix.Output[*StateMachine]{
		OutputState: o.OutputState,
	}
}

func (o StateMachineOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *StateMachine) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o StateMachineOutput) Definition() StateMachineDefinitionPtrOutput {
	return o.ApplyT(func(v *StateMachine) StateMachineDefinitionPtrOutput { return v.Definition }).(StateMachineDefinitionPtrOutput)
}

func (o StateMachineOutput) DefinitionS3Location() StateMachineS3LocationPtrOutput {
	return o.ApplyT(func(v *StateMachine) StateMachineS3LocationPtrOutput { return v.DefinitionS3Location }).(StateMachineS3LocationPtrOutput)
}

func (o StateMachineOutput) DefinitionString() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StateMachine) pulumi.StringPtrOutput { return v.DefinitionString }).(pulumi.StringPtrOutput)
}

func (o StateMachineOutput) DefinitionSubstitutions() StateMachineDefinitionSubstitutionsPtrOutput {
	return o.ApplyT(func(v *StateMachine) StateMachineDefinitionSubstitutionsPtrOutput { return v.DefinitionSubstitutions }).(StateMachineDefinitionSubstitutionsPtrOutput)
}

func (o StateMachineOutput) LoggingConfiguration() StateMachineLoggingConfigurationPtrOutput {
	return o.ApplyT(func(v *StateMachine) StateMachineLoggingConfigurationPtrOutput { return v.LoggingConfiguration }).(StateMachineLoggingConfigurationPtrOutput)
}

func (o StateMachineOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *StateMachine) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o StateMachineOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *StateMachine) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

func (o StateMachineOutput) StateMachineName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StateMachine) pulumi.StringPtrOutput { return v.StateMachineName }).(pulumi.StringPtrOutput)
}

func (o StateMachineOutput) StateMachineRevisionId() pulumi.StringOutput {
	return o.ApplyT(func(v *StateMachine) pulumi.StringOutput { return v.StateMachineRevisionId }).(pulumi.StringOutput)
}

func (o StateMachineOutput) StateMachineType() StateMachineTypePtrOutput {
	return o.ApplyT(func(v *StateMachine) StateMachineTypePtrOutput { return v.StateMachineType }).(StateMachineTypePtrOutput)
}

func (o StateMachineOutput) Tags() StateMachineTagsEntryArrayOutput {
	return o.ApplyT(func(v *StateMachine) StateMachineTagsEntryArrayOutput { return v.Tags }).(StateMachineTagsEntryArrayOutput)
}

func (o StateMachineOutput) TracingConfiguration() StateMachineTracingConfigurationPtrOutput {
	return o.ApplyT(func(v *StateMachine) StateMachineTracingConfigurationPtrOutput { return v.TracingConfiguration }).(StateMachineTracingConfigurationPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StateMachineInput)(nil)).Elem(), &StateMachine{})
	pulumi.RegisterOutputType(StateMachineOutput{})
}

// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package pipes

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::Pipes::Pipe Resource Type
type Pipe struct {
	pulumi.CustomResourceState

	Arn                  pulumi.StringOutput               `pulumi:"arn"`
	CreationTime         pulumi.StringOutput               `pulumi:"creationTime"`
	CurrentState         PipeStateEnumOutput               `pulumi:"currentState"`
	Description          pulumi.StringPtrOutput            `pulumi:"description"`
	DesiredState         PipeRequestedPipeStatePtrOutput   `pulumi:"desiredState"`
	Enrichment           pulumi.StringPtrOutput            `pulumi:"enrichment"`
	EnrichmentParameters PipeEnrichmentParametersPtrOutput `pulumi:"enrichmentParameters"`
	LastModifiedTime     pulumi.StringOutput               `pulumi:"lastModifiedTime"`
	LogConfiguration     PipeLogConfigurationPtrOutput     `pulumi:"logConfiguration"`
	Name                 pulumi.StringPtrOutput            `pulumi:"name"`
	RoleArn              pulumi.StringOutput               `pulumi:"roleArn"`
	Source               pulumi.StringOutput               `pulumi:"source"`
	SourceParameters     PipeSourceParametersPtrOutput     `pulumi:"sourceParameters"`
	StateReason          pulumi.StringOutput               `pulumi:"stateReason"`
	Tags                 PipeTagMapPtrOutput               `pulumi:"tags"`
	Target               pulumi.StringOutput               `pulumi:"target"`
	TargetParameters     PipeTargetParametersPtrOutput     `pulumi:"targetParameters"`
}

// NewPipe registers a new resource with the given unique name, arguments, and options.
func NewPipe(ctx *pulumi.Context,
	name string, args *PipeArgs, opts ...pulumi.ResourceOption) (*Pipe, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	if args.Source == nil {
		return nil, errors.New("invalid value for required argument 'Source'")
	}
	if args.Target == nil {
		return nil, errors.New("invalid value for required argument 'Target'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
		"source",
		"sourceParameters.activeMqBrokerParameters.queueName",
		"sourceParameters.dynamoDbStreamParameters.startingPosition",
		"sourceParameters.kinesisStreamParameters.startingPosition",
		"sourceParameters.kinesisStreamParameters.startingPositionTimestamp",
		"sourceParameters.managedStreamingKafkaParameters.consumerGroupId",
		"sourceParameters.managedStreamingKafkaParameters.startingPosition",
		"sourceParameters.managedStreamingKafkaParameters.topicName",
		"sourceParameters.rabbitMqBrokerParameters.queueName",
		"sourceParameters.rabbitMqBrokerParameters.virtualHost",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Pipe
	err := ctx.RegisterResource("aws-native:pipes:Pipe", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPipe gets an existing Pipe resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPipe(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PipeState, opts ...pulumi.ResourceOption) (*Pipe, error) {
	var resource Pipe
	err := ctx.ReadResource("aws-native:pipes:Pipe", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Pipe resources.
type pipeState struct {
}

type PipeState struct {
}

func (PipeState) ElementType() reflect.Type {
	return reflect.TypeOf((*pipeState)(nil)).Elem()
}

type pipeArgs struct {
	Description          *string                   `pulumi:"description"`
	DesiredState         *PipeRequestedPipeState   `pulumi:"desiredState"`
	Enrichment           *string                   `pulumi:"enrichment"`
	EnrichmentParameters *PipeEnrichmentParameters `pulumi:"enrichmentParameters"`
	LogConfiguration     *PipeLogConfiguration     `pulumi:"logConfiguration"`
	Name                 *string                   `pulumi:"name"`
	RoleArn              string                    `pulumi:"roleArn"`
	Source               string                    `pulumi:"source"`
	SourceParameters     *PipeSourceParameters     `pulumi:"sourceParameters"`
	Tags                 *PipeTagMap               `pulumi:"tags"`
	Target               string                    `pulumi:"target"`
	TargetParameters     *PipeTargetParameters     `pulumi:"targetParameters"`
}

// The set of arguments for constructing a Pipe resource.
type PipeArgs struct {
	Description          pulumi.StringPtrInput
	DesiredState         PipeRequestedPipeStatePtrInput
	Enrichment           pulumi.StringPtrInput
	EnrichmentParameters PipeEnrichmentParametersPtrInput
	LogConfiguration     PipeLogConfigurationPtrInput
	Name                 pulumi.StringPtrInput
	RoleArn              pulumi.StringInput
	Source               pulumi.StringInput
	SourceParameters     PipeSourceParametersPtrInput
	Tags                 PipeTagMapPtrInput
	Target               pulumi.StringInput
	TargetParameters     PipeTargetParametersPtrInput
}

func (PipeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pipeArgs)(nil)).Elem()
}

type PipeInput interface {
	pulumi.Input

	ToPipeOutput() PipeOutput
	ToPipeOutputWithContext(ctx context.Context) PipeOutput
}

func (*Pipe) ElementType() reflect.Type {
	return reflect.TypeOf((**Pipe)(nil)).Elem()
}

func (i *Pipe) ToPipeOutput() PipeOutput {
	return i.ToPipeOutputWithContext(context.Background())
}

func (i *Pipe) ToPipeOutputWithContext(ctx context.Context) PipeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipeOutput)
}

func (i *Pipe) ToOutput(ctx context.Context) pulumix.Output[*Pipe] {
	return pulumix.Output[*Pipe]{
		OutputState: i.ToPipeOutputWithContext(ctx).OutputState,
	}
}

type PipeOutput struct{ *pulumi.OutputState }

func (PipeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Pipe)(nil)).Elem()
}

func (o PipeOutput) ToPipeOutput() PipeOutput {
	return o
}

func (o PipeOutput) ToPipeOutputWithContext(ctx context.Context) PipeOutput {
	return o
}

func (o PipeOutput) ToOutput(ctx context.Context) pulumix.Output[*Pipe] {
	return pulumix.Output[*Pipe]{
		OutputState: o.OutputState,
	}
}

func (o PipeOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o PipeOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

func (o PipeOutput) CurrentState() PipeStateEnumOutput {
	return o.ApplyT(func(v *Pipe) PipeStateEnumOutput { return v.CurrentState }).(PipeStateEnumOutput)
}

func (o PipeOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o PipeOutput) DesiredState() PipeRequestedPipeStatePtrOutput {
	return o.ApplyT(func(v *Pipe) PipeRequestedPipeStatePtrOutput { return v.DesiredState }).(PipeRequestedPipeStatePtrOutput)
}

func (o PipeOutput) Enrichment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringPtrOutput { return v.Enrichment }).(pulumi.StringPtrOutput)
}

func (o PipeOutput) EnrichmentParameters() PipeEnrichmentParametersPtrOutput {
	return o.ApplyT(func(v *Pipe) PipeEnrichmentParametersPtrOutput { return v.EnrichmentParameters }).(PipeEnrichmentParametersPtrOutput)
}

func (o PipeOutput) LastModifiedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringOutput { return v.LastModifiedTime }).(pulumi.StringOutput)
}

func (o PipeOutput) LogConfiguration() PipeLogConfigurationPtrOutput {
	return o.ApplyT(func(v *Pipe) PipeLogConfigurationPtrOutput { return v.LogConfiguration }).(PipeLogConfigurationPtrOutput)
}

func (o PipeOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o PipeOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

func (o PipeOutput) Source() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringOutput { return v.Source }).(pulumi.StringOutput)
}

func (o PipeOutput) SourceParameters() PipeSourceParametersPtrOutput {
	return o.ApplyT(func(v *Pipe) PipeSourceParametersPtrOutput { return v.SourceParameters }).(PipeSourceParametersPtrOutput)
}

func (o PipeOutput) StateReason() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringOutput { return v.StateReason }).(pulumi.StringOutput)
}

func (o PipeOutput) Tags() PipeTagMapPtrOutput {
	return o.ApplyT(func(v *Pipe) PipeTagMapPtrOutput { return v.Tags }).(PipeTagMapPtrOutput)
}

func (o PipeOutput) Target() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipe) pulumi.StringOutput { return v.Target }).(pulumi.StringOutput)
}

func (o PipeOutput) TargetParameters() PipeTargetParametersPtrOutput {
	return o.ApplyT(func(v *Pipe) PipeTargetParametersPtrOutput { return v.TargetParameters }).(PipeTargetParametersPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PipeInput)(nil)).Elem(), &Pipe{})
	pulumi.RegisterOutputType(PipeOutput{})
}

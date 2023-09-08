// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package transfer

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Transfer::Workflow
type Workflow struct {
	pulumi.CustomResourceState

	// Specifies the unique Amazon Resource Name (ARN) for the workflow.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A textual description for the workflow.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Specifies the steps (actions) to take if any errors are encountered during execution of the workflow.
	OnExceptionSteps WorkflowStepArrayOutput `pulumi:"onExceptionSteps"`
	// Specifies the details for the steps that are in the specified workflow.
	Steps WorkflowStepArrayOutput `pulumi:"steps"`
	// Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
	Tags WorkflowTagArrayOutput `pulumi:"tags"`
	// A unique identifier for the workflow.
	WorkflowId pulumi.StringOutput `pulumi:"workflowId"`
}

// NewWorkflow registers a new resource with the given unique name, arguments, and options.
func NewWorkflow(ctx *pulumi.Context,
	name string, args *WorkflowArgs, opts ...pulumi.ResourceOption) (*Workflow, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Steps == nil {
		return nil, errors.New("invalid value for required argument 'Steps'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"description",
		"onExceptionSteps[*]",
		"steps[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Workflow
	err := ctx.RegisterResource("aws-native:transfer:Workflow", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWorkflow gets an existing Workflow resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWorkflow(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WorkflowState, opts ...pulumi.ResourceOption) (*Workflow, error) {
	var resource Workflow
	err := ctx.ReadResource("aws-native:transfer:Workflow", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Workflow resources.
type workflowState struct {
}

type WorkflowState struct {
}

func (WorkflowState) ElementType() reflect.Type {
	return reflect.TypeOf((*workflowState)(nil)).Elem()
}

type workflowArgs struct {
	// A textual description for the workflow.
	Description *string `pulumi:"description"`
	// Specifies the steps (actions) to take if any errors are encountered during execution of the workflow.
	OnExceptionSteps []WorkflowStep `pulumi:"onExceptionSteps"`
	// Specifies the details for the steps that are in the specified workflow.
	Steps []WorkflowStep `pulumi:"steps"`
	// Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
	Tags []WorkflowTag `pulumi:"tags"`
}

// The set of arguments for constructing a Workflow resource.
type WorkflowArgs struct {
	// A textual description for the workflow.
	Description pulumi.StringPtrInput
	// Specifies the steps (actions) to take if any errors are encountered during execution of the workflow.
	OnExceptionSteps WorkflowStepArrayInput
	// Specifies the details for the steps that are in the specified workflow.
	Steps WorkflowStepArrayInput
	// Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
	Tags WorkflowTagArrayInput
}

func (WorkflowArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*workflowArgs)(nil)).Elem()
}

type WorkflowInput interface {
	pulumi.Input

	ToWorkflowOutput() WorkflowOutput
	ToWorkflowOutputWithContext(ctx context.Context) WorkflowOutput
}

func (*Workflow) ElementType() reflect.Type {
	return reflect.TypeOf((**Workflow)(nil)).Elem()
}

func (i *Workflow) ToWorkflowOutput() WorkflowOutput {
	return i.ToWorkflowOutputWithContext(context.Background())
}

func (i *Workflow) ToWorkflowOutputWithContext(ctx context.Context) WorkflowOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkflowOutput)
}

func (i *Workflow) ToOutput(ctx context.Context) pulumix.Output[*Workflow] {
	return pulumix.Output[*Workflow]{
		OutputState: i.ToWorkflowOutputWithContext(ctx).OutputState,
	}
}

type WorkflowOutput struct{ *pulumi.OutputState }

func (WorkflowOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Workflow)(nil)).Elem()
}

func (o WorkflowOutput) ToWorkflowOutput() WorkflowOutput {
	return o
}

func (o WorkflowOutput) ToWorkflowOutputWithContext(ctx context.Context) WorkflowOutput {
	return o
}

func (o WorkflowOutput) ToOutput(ctx context.Context) pulumix.Output[*Workflow] {
	return pulumix.Output[*Workflow]{
		OutputState: o.OutputState,
	}
}

// Specifies the unique Amazon Resource Name (ARN) for the workflow.
func (o WorkflowOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Workflow) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// A textual description for the workflow.
func (o WorkflowOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Workflow) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Specifies the steps (actions) to take if any errors are encountered during execution of the workflow.
func (o WorkflowOutput) OnExceptionSteps() WorkflowStepArrayOutput {
	return o.ApplyT(func(v *Workflow) WorkflowStepArrayOutput { return v.OnExceptionSteps }).(WorkflowStepArrayOutput)
}

// Specifies the details for the steps that are in the specified workflow.
func (o WorkflowOutput) Steps() WorkflowStepArrayOutput {
	return o.ApplyT(func(v *Workflow) WorkflowStepArrayOutput { return v.Steps }).(WorkflowStepArrayOutput)
}

// Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
func (o WorkflowOutput) Tags() WorkflowTagArrayOutput {
	return o.ApplyT(func(v *Workflow) WorkflowTagArrayOutput { return v.Tags }).(WorkflowTagArrayOutput)
}

// A unique identifier for the workflow.
func (o WorkflowOutput) WorkflowId() pulumi.StringOutput {
	return o.ApplyT(func(v *Workflow) pulumi.StringOutput { return v.WorkflowId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WorkflowInput)(nil)).Elem(), &Workflow{})
	pulumi.RegisterOutputType(WorkflowOutput{})
}

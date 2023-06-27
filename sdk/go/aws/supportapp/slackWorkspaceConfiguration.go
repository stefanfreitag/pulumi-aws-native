// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package supportapp

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// An AWS Support App resource that creates, updates, lists, and deletes Slack workspace configurations.
type SlackWorkspaceConfiguration struct {
	pulumi.CustomResourceState

	// The team ID in Slack, which uniquely identifies a workspace.
	TeamId pulumi.StringOutput `pulumi:"teamId"`
	// An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.
	VersionId pulumi.StringPtrOutput `pulumi:"versionId"`
}

// NewSlackWorkspaceConfiguration registers a new resource with the given unique name, arguments, and options.
func NewSlackWorkspaceConfiguration(ctx *pulumi.Context,
	name string, args *SlackWorkspaceConfigurationArgs, opts ...pulumi.ResourceOption) (*SlackWorkspaceConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.TeamId == nil {
		return nil, errors.New("invalid value for required argument 'TeamId'")
	}
	var resource SlackWorkspaceConfiguration
	err := ctx.RegisterResource("aws-native:supportapp:SlackWorkspaceConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSlackWorkspaceConfiguration gets an existing SlackWorkspaceConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSlackWorkspaceConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SlackWorkspaceConfigurationState, opts ...pulumi.ResourceOption) (*SlackWorkspaceConfiguration, error) {
	var resource SlackWorkspaceConfiguration
	err := ctx.ReadResource("aws-native:supportapp:SlackWorkspaceConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SlackWorkspaceConfiguration resources.
type slackWorkspaceConfigurationState struct {
}

type SlackWorkspaceConfigurationState struct {
}

func (SlackWorkspaceConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*slackWorkspaceConfigurationState)(nil)).Elem()
}

type slackWorkspaceConfigurationArgs struct {
	// The team ID in Slack, which uniquely identifies a workspace.
	TeamId string `pulumi:"teamId"`
	// An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.
	VersionId *string `pulumi:"versionId"`
}

// The set of arguments for constructing a SlackWorkspaceConfiguration resource.
type SlackWorkspaceConfigurationArgs struct {
	// The team ID in Slack, which uniquely identifies a workspace.
	TeamId pulumi.StringInput
	// An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.
	VersionId pulumi.StringPtrInput
}

func (SlackWorkspaceConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*slackWorkspaceConfigurationArgs)(nil)).Elem()
}

type SlackWorkspaceConfigurationInput interface {
	pulumi.Input

	ToSlackWorkspaceConfigurationOutput() SlackWorkspaceConfigurationOutput
	ToSlackWorkspaceConfigurationOutputWithContext(ctx context.Context) SlackWorkspaceConfigurationOutput
}

func (*SlackWorkspaceConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((**SlackWorkspaceConfiguration)(nil)).Elem()
}

func (i *SlackWorkspaceConfiguration) ToSlackWorkspaceConfigurationOutput() SlackWorkspaceConfigurationOutput {
	return i.ToSlackWorkspaceConfigurationOutputWithContext(context.Background())
}

func (i *SlackWorkspaceConfiguration) ToSlackWorkspaceConfigurationOutputWithContext(ctx context.Context) SlackWorkspaceConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SlackWorkspaceConfigurationOutput)
}

type SlackWorkspaceConfigurationOutput struct{ *pulumi.OutputState }

func (SlackWorkspaceConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SlackWorkspaceConfiguration)(nil)).Elem()
}

func (o SlackWorkspaceConfigurationOutput) ToSlackWorkspaceConfigurationOutput() SlackWorkspaceConfigurationOutput {
	return o
}

func (o SlackWorkspaceConfigurationOutput) ToSlackWorkspaceConfigurationOutputWithContext(ctx context.Context) SlackWorkspaceConfigurationOutput {
	return o
}

// The team ID in Slack, which uniquely identifies a workspace.
func (o SlackWorkspaceConfigurationOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v *SlackWorkspaceConfiguration) pulumi.StringOutput { return v.TeamId }).(pulumi.StringOutput)
}

// An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.
func (o SlackWorkspaceConfigurationOutput) VersionId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SlackWorkspaceConfiguration) pulumi.StringPtrOutput { return v.VersionId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SlackWorkspaceConfigurationInput)(nil)).Elem(), &SlackWorkspaceConfiguration{})
	pulumi.RegisterOutputType(SlackWorkspaceConfigurationOutput{})
}

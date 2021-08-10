// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package chatbot

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html
type SlackChannelConfiguration struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-configurationname
	ConfigurationName pulumi.StringOutput `pulumi:"configurationName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-iamrolearn
	IamRoleArn pulumi.StringOutput `pulumi:"iamRoleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-logginglevel
	LoggingLevel pulumi.StringPtrOutput `pulumi:"loggingLevel"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackchannelid
	SlackChannelId pulumi.StringOutput `pulumi:"slackChannelId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackworkspaceid
	SlackWorkspaceId pulumi.StringOutput `pulumi:"slackWorkspaceId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-snstopicarns
	SnsTopicArns pulumi.StringArrayOutput `pulumi:"snsTopicArns"`
}

// NewSlackChannelConfiguration registers a new resource with the given unique name, arguments, and options.
func NewSlackChannelConfiguration(ctx *pulumi.Context,
	name string, args *SlackChannelConfigurationArgs, opts ...pulumi.ResourceOption) (*SlackChannelConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConfigurationName == nil {
		return nil, errors.New("invalid value for required argument 'ConfigurationName'")
	}
	if args.IamRoleArn == nil {
		return nil, errors.New("invalid value for required argument 'IamRoleArn'")
	}
	if args.SlackChannelId == nil {
		return nil, errors.New("invalid value for required argument 'SlackChannelId'")
	}
	if args.SlackWorkspaceId == nil {
		return nil, errors.New("invalid value for required argument 'SlackWorkspaceId'")
	}
	var resource SlackChannelConfiguration
	err := ctx.RegisterResource("aws-native:Chatbot:SlackChannelConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSlackChannelConfiguration gets an existing SlackChannelConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSlackChannelConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SlackChannelConfigurationState, opts ...pulumi.ResourceOption) (*SlackChannelConfiguration, error) {
	var resource SlackChannelConfiguration
	err := ctx.ReadResource("aws-native:Chatbot:SlackChannelConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SlackChannelConfiguration resources.
type slackChannelConfigurationState struct {
}

type SlackChannelConfigurationState struct {
}

func (SlackChannelConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*slackChannelConfigurationState)(nil)).Elem()
}

type slackChannelConfigurationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-configurationname
	ConfigurationName string `pulumi:"configurationName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-iamrolearn
	IamRoleArn string `pulumi:"iamRoleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-logginglevel
	LoggingLevel *string `pulumi:"loggingLevel"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackchannelid
	SlackChannelId string `pulumi:"slackChannelId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackworkspaceid
	SlackWorkspaceId string `pulumi:"slackWorkspaceId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-snstopicarns
	SnsTopicArns []string `pulumi:"snsTopicArns"`
}

// The set of arguments for constructing a SlackChannelConfiguration resource.
type SlackChannelConfigurationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-configurationname
	ConfigurationName pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-iamrolearn
	IamRoleArn pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-logginglevel
	LoggingLevel pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackchannelid
	SlackChannelId pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackworkspaceid
	SlackWorkspaceId pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-snstopicarns
	SnsTopicArns pulumi.StringArrayInput
}

func (SlackChannelConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*slackChannelConfigurationArgs)(nil)).Elem()
}

type SlackChannelConfigurationInput interface {
	pulumi.Input

	ToSlackChannelConfigurationOutput() SlackChannelConfigurationOutput
	ToSlackChannelConfigurationOutputWithContext(ctx context.Context) SlackChannelConfigurationOutput
}

func (*SlackChannelConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((*SlackChannelConfiguration)(nil))
}

func (i *SlackChannelConfiguration) ToSlackChannelConfigurationOutput() SlackChannelConfigurationOutput {
	return i.ToSlackChannelConfigurationOutputWithContext(context.Background())
}

func (i *SlackChannelConfiguration) ToSlackChannelConfigurationOutputWithContext(ctx context.Context) SlackChannelConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SlackChannelConfigurationOutput)
}

type SlackChannelConfigurationOutput struct{ *pulumi.OutputState }

func (SlackChannelConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SlackChannelConfiguration)(nil))
}

func (o SlackChannelConfigurationOutput) ToSlackChannelConfigurationOutput() SlackChannelConfigurationOutput {
	return o
}

func (o SlackChannelConfigurationOutput) ToSlackChannelConfigurationOutputWithContext(ctx context.Context) SlackChannelConfigurationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(SlackChannelConfigurationOutput{})
}

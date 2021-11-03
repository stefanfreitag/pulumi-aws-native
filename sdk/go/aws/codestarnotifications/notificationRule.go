// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package codestarnotifications

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CodeStarNotifications::NotificationRule
type NotificationRule struct {
	pulumi.CustomResourceState

	Arn           pulumi.StringOutput               `pulumi:"arn"`
	CreatedBy     pulumi.StringPtrOutput            `pulumi:"createdBy"`
	DetailType    NotificationRuleDetailTypeOutput  `pulumi:"detailType"`
	EventTypeId   pulumi.StringPtrOutput            `pulumi:"eventTypeId"`
	EventTypeIds  pulumi.StringArrayOutput          `pulumi:"eventTypeIds"`
	Name          pulumi.StringOutput               `pulumi:"name"`
	Resource      pulumi.StringOutput               `pulumi:"resource"`
	Status        NotificationRuleStatusPtrOutput   `pulumi:"status"`
	Tags          pulumi.AnyOutput                  `pulumi:"tags"`
	TargetAddress pulumi.StringPtrOutput            `pulumi:"targetAddress"`
	Targets       NotificationRuleTargetArrayOutput `pulumi:"targets"`
}

// NewNotificationRule registers a new resource with the given unique name, arguments, and options.
func NewNotificationRule(ctx *pulumi.Context,
	name string, args *NotificationRuleArgs, opts ...pulumi.ResourceOption) (*NotificationRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DetailType == nil {
		return nil, errors.New("invalid value for required argument 'DetailType'")
	}
	if args.EventTypeIds == nil {
		return nil, errors.New("invalid value for required argument 'EventTypeIds'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.Resource == nil {
		return nil, errors.New("invalid value for required argument 'Resource'")
	}
	if args.Targets == nil {
		return nil, errors.New("invalid value for required argument 'Targets'")
	}
	var resource NotificationRule
	err := ctx.RegisterResource("aws-native:codestarnotifications:NotificationRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNotificationRule gets an existing NotificationRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNotificationRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NotificationRuleState, opts ...pulumi.ResourceOption) (*NotificationRule, error) {
	var resource NotificationRule
	err := ctx.ReadResource("aws-native:codestarnotifications:NotificationRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NotificationRule resources.
type notificationRuleState struct {
}

type NotificationRuleState struct {
}

func (NotificationRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*notificationRuleState)(nil)).Elem()
}

type notificationRuleArgs struct {
	CreatedBy     *string                    `pulumi:"createdBy"`
	DetailType    NotificationRuleDetailType `pulumi:"detailType"`
	EventTypeId   *string                    `pulumi:"eventTypeId"`
	EventTypeIds  []string                   `pulumi:"eventTypeIds"`
	Name          string                     `pulumi:"name"`
	Resource      string                     `pulumi:"resource"`
	Status        *NotificationRuleStatus    `pulumi:"status"`
	Tags          interface{}                `pulumi:"tags"`
	TargetAddress *string                    `pulumi:"targetAddress"`
	Targets       []NotificationRuleTarget   `pulumi:"targets"`
}

// The set of arguments for constructing a NotificationRule resource.
type NotificationRuleArgs struct {
	CreatedBy     pulumi.StringPtrInput
	DetailType    NotificationRuleDetailTypeInput
	EventTypeId   pulumi.StringPtrInput
	EventTypeIds  pulumi.StringArrayInput
	Name          pulumi.StringInput
	Resource      pulumi.StringInput
	Status        NotificationRuleStatusPtrInput
	Tags          pulumi.Input
	TargetAddress pulumi.StringPtrInput
	Targets       NotificationRuleTargetArrayInput
}

func (NotificationRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*notificationRuleArgs)(nil)).Elem()
}

type NotificationRuleInput interface {
	pulumi.Input

	ToNotificationRuleOutput() NotificationRuleOutput
	ToNotificationRuleOutputWithContext(ctx context.Context) NotificationRuleOutput
}

func (*NotificationRule) ElementType() reflect.Type {
	return reflect.TypeOf((*NotificationRule)(nil))
}

func (i *NotificationRule) ToNotificationRuleOutput() NotificationRuleOutput {
	return i.ToNotificationRuleOutputWithContext(context.Background())
}

func (i *NotificationRule) ToNotificationRuleOutputWithContext(ctx context.Context) NotificationRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRuleOutput)
}

type NotificationRuleOutput struct{ *pulumi.OutputState }

func (NotificationRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*NotificationRule)(nil))
}

func (o NotificationRuleOutput) ToNotificationRuleOutput() NotificationRuleOutput {
	return o
}

func (o NotificationRuleOutput) ToNotificationRuleOutputWithContext(ctx context.Context) NotificationRuleOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NotificationRuleInput)(nil)).Elem(), &NotificationRule{})
	pulumi.RegisterOutputType(NotificationRuleOutput{})
}

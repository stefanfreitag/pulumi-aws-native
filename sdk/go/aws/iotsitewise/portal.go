// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iotsitewise

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::IoTSiteWise::Portal
type Portal struct {
	pulumi.CustomResourceState

	// Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range.
	Alarms AlarmsPropertiesPtrOutput `pulumi:"alarms"`
	// The email address that sends alarm notifications.
	NotificationSenderEmail pulumi.StringPtrOutput `pulumi:"notificationSenderEmail"`
	// The ARN of the portal, which has the following format.
	PortalArn pulumi.StringOutput `pulumi:"portalArn"`
	// The service to use to authenticate users to the portal. Choose from SSO or IAM. You can't change this value after you create a portal.
	PortalAuthMode pulumi.StringPtrOutput `pulumi:"portalAuthMode"`
	// The AWS SSO application generated client ID (used with AWS SSO APIs).
	PortalClientId pulumi.StringOutput `pulumi:"portalClientId"`
	// The AWS administrator's contact email address.
	PortalContactEmail pulumi.StringOutput `pulumi:"portalContactEmail"`
	// A description for the portal.
	PortalDescription pulumi.StringPtrOutput `pulumi:"portalDescription"`
	// The ID of the portal.
	PortalId pulumi.StringOutput `pulumi:"portalId"`
	// A friendly name for the portal.
	PortalName pulumi.StringOutput `pulumi:"portalName"`
	// The public root URL for the AWS IoT AWS IoT SiteWise Monitor application portal.
	PortalStartUrl pulumi.StringOutput `pulumi:"portalStartUrl"`
	// The ARN of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf.
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// A list of key-value pairs that contain metadata for the portal.
	Tags PortalTagArrayOutput `pulumi:"tags"`
}

// NewPortal registers a new resource with the given unique name, arguments, and options.
func NewPortal(ctx *pulumi.Context,
	name string, args *PortalArgs, opts ...pulumi.ResourceOption) (*Portal, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PortalContactEmail == nil {
		return nil, errors.New("invalid value for required argument 'PortalContactEmail'")
	}
	if args.PortalName == nil {
		return nil, errors.New("invalid value for required argument 'PortalName'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource Portal
	err := ctx.RegisterResource("aws-native:iotsitewise:Portal", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPortal gets an existing Portal resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPortal(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PortalState, opts ...pulumi.ResourceOption) (*Portal, error) {
	var resource Portal
	err := ctx.ReadResource("aws-native:iotsitewise:Portal", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Portal resources.
type portalState struct {
}

type PortalState struct {
}

func (PortalState) ElementType() reflect.Type {
	return reflect.TypeOf((*portalState)(nil)).Elem()
}

type portalArgs struct {
	// Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range.
	Alarms *AlarmsProperties `pulumi:"alarms"`
	// The email address that sends alarm notifications.
	NotificationSenderEmail *string `pulumi:"notificationSenderEmail"`
	// The service to use to authenticate users to the portal. Choose from SSO or IAM. You can't change this value after you create a portal.
	PortalAuthMode *string `pulumi:"portalAuthMode"`
	// The AWS administrator's contact email address.
	PortalContactEmail string `pulumi:"portalContactEmail"`
	// A description for the portal.
	PortalDescription *string `pulumi:"portalDescription"`
	// A friendly name for the portal.
	PortalName string `pulumi:"portalName"`
	// The ARN of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf.
	RoleArn string `pulumi:"roleArn"`
	// A list of key-value pairs that contain metadata for the portal.
	Tags []PortalTag `pulumi:"tags"`
}

// The set of arguments for constructing a Portal resource.
type PortalArgs struct {
	// Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range.
	Alarms AlarmsPropertiesPtrInput
	// The email address that sends alarm notifications.
	NotificationSenderEmail pulumi.StringPtrInput
	// The service to use to authenticate users to the portal. Choose from SSO or IAM. You can't change this value after you create a portal.
	PortalAuthMode pulumi.StringPtrInput
	// The AWS administrator's contact email address.
	PortalContactEmail pulumi.StringInput
	// A description for the portal.
	PortalDescription pulumi.StringPtrInput
	// A friendly name for the portal.
	PortalName pulumi.StringInput
	// The ARN of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf.
	RoleArn pulumi.StringInput
	// A list of key-value pairs that contain metadata for the portal.
	Tags PortalTagArrayInput
}

func (PortalArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*portalArgs)(nil)).Elem()
}

type PortalInput interface {
	pulumi.Input

	ToPortalOutput() PortalOutput
	ToPortalOutputWithContext(ctx context.Context) PortalOutput
}

func (*Portal) ElementType() reflect.Type {
	return reflect.TypeOf((*Portal)(nil))
}

func (i *Portal) ToPortalOutput() PortalOutput {
	return i.ToPortalOutputWithContext(context.Background())
}

func (i *Portal) ToPortalOutputWithContext(ctx context.Context) PortalOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PortalOutput)
}

type PortalOutput struct{ *pulumi.OutputState }

func (PortalOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Portal)(nil))
}

func (o PortalOutput) ToPortalOutput() PortalOutput {
	return o
}

func (o PortalOutput) ToPortalOutputWithContext(ctx context.Context) PortalOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PortalInput)(nil)).Elem(), &Portal{})
	pulumi.RegisterOutputType(PortalOutput{})
}

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticache

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ElastiCache::UserGroup
type UserGroup struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the user account.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Must be redis.
	Engine UserGroupEngineOutput `pulumi:"engine"`
	// Indicates user group status. Can be "creating", "active", "modifying", "deleting".
	Status pulumi.StringOutput `pulumi:"status"`
	// The ID of the user group.
	UserGroupId pulumi.StringOutput `pulumi:"userGroupId"`
	// List of users associated to this user group.
	UserIds pulumi.StringArrayOutput `pulumi:"userIds"`
}

// NewUserGroup registers a new resource with the given unique name, arguments, and options.
func NewUserGroup(ctx *pulumi.Context,
	name string, args *UserGroupArgs, opts ...pulumi.ResourceOption) (*UserGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Engine == nil {
		return nil, errors.New("invalid value for required argument 'Engine'")
	}
	if args.UserGroupId == nil {
		return nil, errors.New("invalid value for required argument 'UserGroupId'")
	}
	var resource UserGroup
	err := ctx.RegisterResource("aws-native:elasticache:UserGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserGroup gets an existing UserGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserGroupState, opts ...pulumi.ResourceOption) (*UserGroup, error) {
	var resource UserGroup
	err := ctx.ReadResource("aws-native:elasticache:UserGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserGroup resources.
type userGroupState struct {
}

type UserGroupState struct {
}

func (UserGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*userGroupState)(nil)).Elem()
}

type userGroupArgs struct {
	// Must be redis.
	Engine UserGroupEngine `pulumi:"engine"`
	// The ID of the user group.
	UserGroupId string `pulumi:"userGroupId"`
	// List of users associated to this user group.
	UserIds []string `pulumi:"userIds"`
}

// The set of arguments for constructing a UserGroup resource.
type UserGroupArgs struct {
	// Must be redis.
	Engine UserGroupEngineInput
	// The ID of the user group.
	UserGroupId pulumi.StringInput
	// List of users associated to this user group.
	UserIds pulumi.StringArrayInput
}

func (UserGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userGroupArgs)(nil)).Elem()
}

type UserGroupInput interface {
	pulumi.Input

	ToUserGroupOutput() UserGroupOutput
	ToUserGroupOutputWithContext(ctx context.Context) UserGroupOutput
}

func (*UserGroup) ElementType() reflect.Type {
	return reflect.TypeOf((*UserGroup)(nil))
}

func (i *UserGroup) ToUserGroupOutput() UserGroupOutput {
	return i.ToUserGroupOutputWithContext(context.Background())
}

func (i *UserGroup) ToUserGroupOutputWithContext(ctx context.Context) UserGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserGroupOutput)
}

type UserGroupOutput struct{ *pulumi.OutputState }

func (UserGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserGroup)(nil))
}

func (o UserGroupOutput) ToUserGroupOutput() UserGroupOutput {
	return o
}

func (o UserGroupOutput) ToUserGroupOutputWithContext(ctx context.Context) UserGroupOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(UserGroupOutput{})
}

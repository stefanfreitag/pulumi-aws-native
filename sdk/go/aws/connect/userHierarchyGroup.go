// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package connect

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Connect::UserHierarchyGroup
type UserHierarchyGroup struct {
	pulumi.CustomResourceState

	// The identifier of the Amazon Connect instance.
	InstanceArn pulumi.StringOutput `pulumi:"instanceArn"`
	// The name of the user hierarchy group.
	Name pulumi.StringOutput `pulumi:"name"`
	// The Amazon Resource Name (ARN) for the parent user hierarchy group.
	ParentGroupArn pulumi.StringPtrOutput `pulumi:"parentGroupArn"`
	// The Amazon Resource Name (ARN) for the user hierarchy group.
	UserHierarchyGroupArn pulumi.StringOutput `pulumi:"userHierarchyGroupArn"`
}

// NewUserHierarchyGroup registers a new resource with the given unique name, arguments, and options.
func NewUserHierarchyGroup(ctx *pulumi.Context,
	name string, args *UserHierarchyGroupArgs, opts ...pulumi.ResourceOption) (*UserHierarchyGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceArn == nil {
		return nil, errors.New("invalid value for required argument 'InstanceArn'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource UserHierarchyGroup
	err := ctx.RegisterResource("aws-native:connect:UserHierarchyGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserHierarchyGroup gets an existing UserHierarchyGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserHierarchyGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserHierarchyGroupState, opts ...pulumi.ResourceOption) (*UserHierarchyGroup, error) {
	var resource UserHierarchyGroup
	err := ctx.ReadResource("aws-native:connect:UserHierarchyGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserHierarchyGroup resources.
type userHierarchyGroupState struct {
}

type UserHierarchyGroupState struct {
}

func (UserHierarchyGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*userHierarchyGroupState)(nil)).Elem()
}

type userHierarchyGroupArgs struct {
	// The identifier of the Amazon Connect instance.
	InstanceArn string `pulumi:"instanceArn"`
	// The name of the user hierarchy group.
	Name string `pulumi:"name"`
	// The Amazon Resource Name (ARN) for the parent user hierarchy group.
	ParentGroupArn *string `pulumi:"parentGroupArn"`
}

// The set of arguments for constructing a UserHierarchyGroup resource.
type UserHierarchyGroupArgs struct {
	// The identifier of the Amazon Connect instance.
	InstanceArn pulumi.StringInput
	// The name of the user hierarchy group.
	Name pulumi.StringInput
	// The Amazon Resource Name (ARN) for the parent user hierarchy group.
	ParentGroupArn pulumi.StringPtrInput
}

func (UserHierarchyGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userHierarchyGroupArgs)(nil)).Elem()
}

type UserHierarchyGroupInput interface {
	pulumi.Input

	ToUserHierarchyGroupOutput() UserHierarchyGroupOutput
	ToUserHierarchyGroupOutputWithContext(ctx context.Context) UserHierarchyGroupOutput
}

func (*UserHierarchyGroup) ElementType() reflect.Type {
	return reflect.TypeOf((*UserHierarchyGroup)(nil))
}

func (i *UserHierarchyGroup) ToUserHierarchyGroupOutput() UserHierarchyGroupOutput {
	return i.ToUserHierarchyGroupOutputWithContext(context.Background())
}

func (i *UserHierarchyGroup) ToUserHierarchyGroupOutputWithContext(ctx context.Context) UserHierarchyGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserHierarchyGroupOutput)
}

type UserHierarchyGroupOutput struct{ *pulumi.OutputState }

func (UserHierarchyGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserHierarchyGroup)(nil))
}

func (o UserHierarchyGroupOutput) ToUserHierarchyGroupOutput() UserHierarchyGroupOutput {
	return o
}

func (o UserHierarchyGroupOutput) ToUserHierarchyGroupOutputWithContext(ctx context.Context) UserHierarchyGroupOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserHierarchyGroupInput)(nil)).Elem(), &UserHierarchyGroup{})
	pulumi.RegisterOutputType(UserHierarchyGroupOutput{})
}

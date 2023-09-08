// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gamelift

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.
func LookupGameServerGroup(ctx *pulumi.Context, args *LookupGameServerGroupArgs, opts ...pulumi.InvokeOption) (*LookupGameServerGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupGameServerGroupResult
	err := ctx.Invoke("aws-native:gamelift:getGameServerGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupGameServerGroupArgs struct {
	// A generated unique ID for the game server group.
	GameServerGroupArn string `pulumi:"gameServerGroupArn"`
}

type LookupGameServerGroupResult struct {
	// A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.
	AutoScalingGroupArn *string `pulumi:"autoScalingGroupArn"`
	// The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
	BalancingStrategy *GameServerGroupBalancingStrategy `pulumi:"balancingStrategy"`
	// A generated unique ID for the game server group.
	GameServerGroupArn *string `pulumi:"gameServerGroupArn"`
	// An identifier for the new game server group.
	GameServerGroupName *string `pulumi:"gameServerGroupName"`
	// A flag that indicates whether instances in the game server group are protected from early termination.
	GameServerProtectionPolicy *GameServerGroupGameServerProtectionPolicy `pulumi:"gameServerProtectionPolicy"`
	// A set of EC2 instance types to use when creating instances in the group.
	InstanceDefinitions []GameServerGroupInstanceDefinition `pulumi:"instanceDefinitions"`
	// The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
	RoleArn *string `pulumi:"roleArn"`
}

func LookupGameServerGroupOutput(ctx *pulumi.Context, args LookupGameServerGroupOutputArgs, opts ...pulumi.InvokeOption) LookupGameServerGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGameServerGroupResult, error) {
			args := v.(LookupGameServerGroupArgs)
			r, err := LookupGameServerGroup(ctx, &args, opts...)
			var s LookupGameServerGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupGameServerGroupResultOutput)
}

type LookupGameServerGroupOutputArgs struct {
	// A generated unique ID for the game server group.
	GameServerGroupArn pulumi.StringInput `pulumi:"gameServerGroupArn"`
}

func (LookupGameServerGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGameServerGroupArgs)(nil)).Elem()
}

type LookupGameServerGroupResultOutput struct{ *pulumi.OutputState }

func (LookupGameServerGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGameServerGroupResult)(nil)).Elem()
}

func (o LookupGameServerGroupResultOutput) ToLookupGameServerGroupResultOutput() LookupGameServerGroupResultOutput {
	return o
}

func (o LookupGameServerGroupResultOutput) ToLookupGameServerGroupResultOutputWithContext(ctx context.Context) LookupGameServerGroupResultOutput {
	return o
}

func (o LookupGameServerGroupResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupGameServerGroupResult] {
	return pulumix.Output[LookupGameServerGroupResult]{
		OutputState: o.OutputState,
	}
}

// A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.
func (o LookupGameServerGroupResultOutput) AutoScalingGroupArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGameServerGroupResult) *string { return v.AutoScalingGroupArn }).(pulumi.StringPtrOutput)
}

// The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
func (o LookupGameServerGroupResultOutput) BalancingStrategy() GameServerGroupBalancingStrategyPtrOutput {
	return o.ApplyT(func(v LookupGameServerGroupResult) *GameServerGroupBalancingStrategy { return v.BalancingStrategy }).(GameServerGroupBalancingStrategyPtrOutput)
}

// A generated unique ID for the game server group.
func (o LookupGameServerGroupResultOutput) GameServerGroupArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGameServerGroupResult) *string { return v.GameServerGroupArn }).(pulumi.StringPtrOutput)
}

// An identifier for the new game server group.
func (o LookupGameServerGroupResultOutput) GameServerGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGameServerGroupResult) *string { return v.GameServerGroupName }).(pulumi.StringPtrOutput)
}

// A flag that indicates whether instances in the game server group are protected from early termination.
func (o LookupGameServerGroupResultOutput) GameServerProtectionPolicy() GameServerGroupGameServerProtectionPolicyPtrOutput {
	return o.ApplyT(func(v LookupGameServerGroupResult) *GameServerGroupGameServerProtectionPolicy {
		return v.GameServerProtectionPolicy
	}).(GameServerGroupGameServerProtectionPolicyPtrOutput)
}

// A set of EC2 instance types to use when creating instances in the group.
func (o LookupGameServerGroupResultOutput) InstanceDefinitions() GameServerGroupInstanceDefinitionArrayOutput {
	return o.ApplyT(func(v LookupGameServerGroupResult) []GameServerGroupInstanceDefinition { return v.InstanceDefinitions }).(GameServerGroupInstanceDefinitionArrayOutput)
}

// The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
func (o LookupGameServerGroupResultOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGameServerGroupResult) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGameServerGroupResultOutput{})
}

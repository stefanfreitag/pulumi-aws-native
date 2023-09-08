// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package autoscaling

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::AutoScaling::LifecycleHook
func LookupLifecycleHook(ctx *pulumi.Context, args *LookupLifecycleHookArgs, opts ...pulumi.InvokeOption) (*LookupLifecycleHookResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLifecycleHookResult
	err := ctx.Invoke("aws-native:autoscaling:getLifecycleHook", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLifecycleHookArgs struct {
	// The name of the Auto Scaling group for the lifecycle hook.
	AutoScalingGroupName string `pulumi:"autoScalingGroupName"`
	// The name of the lifecycle hook.
	LifecycleHookName string `pulumi:"lifecycleHookName"`
}

type LookupLifecycleHookResult struct {
	// The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are CONTINUE and ABANDON (default).
	DefaultResult *string `pulumi:"defaultResult"`
	// The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default value is 3600 seconds (1 hour). If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult property.
	HeartbeatTimeout *int `pulumi:"heartbeatTimeout"`
	// The instance state to which you want to attach the lifecycle hook.
	LifecycleTransition *string `pulumi:"lifecycleTransition"`
	// Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.
	NotificationMetadata *string `pulumi:"notificationMetadata"`
	// The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. You can specify an Amazon SQS queue or an Amazon SNS topic. The notification message includes the following information: lifecycle action token, user account ID, Auto Scaling group name, lifecycle hook name, instance ID, lifecycle transition, and notification metadata.
	NotificationTargetArn *string `pulumi:"notificationTargetArn"`
	// The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.
	RoleArn *string `pulumi:"roleArn"`
}

func LookupLifecycleHookOutput(ctx *pulumi.Context, args LookupLifecycleHookOutputArgs, opts ...pulumi.InvokeOption) LookupLifecycleHookResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLifecycleHookResult, error) {
			args := v.(LookupLifecycleHookArgs)
			r, err := LookupLifecycleHook(ctx, &args, opts...)
			var s LookupLifecycleHookResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLifecycleHookResultOutput)
}

type LookupLifecycleHookOutputArgs struct {
	// The name of the Auto Scaling group for the lifecycle hook.
	AutoScalingGroupName pulumi.StringInput `pulumi:"autoScalingGroupName"`
	// The name of the lifecycle hook.
	LifecycleHookName pulumi.StringInput `pulumi:"lifecycleHookName"`
}

func (LookupLifecycleHookOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLifecycleHookArgs)(nil)).Elem()
}

type LookupLifecycleHookResultOutput struct{ *pulumi.OutputState }

func (LookupLifecycleHookResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLifecycleHookResult)(nil)).Elem()
}

func (o LookupLifecycleHookResultOutput) ToLookupLifecycleHookResultOutput() LookupLifecycleHookResultOutput {
	return o
}

func (o LookupLifecycleHookResultOutput) ToLookupLifecycleHookResultOutputWithContext(ctx context.Context) LookupLifecycleHookResultOutput {
	return o
}

func (o LookupLifecycleHookResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupLifecycleHookResult] {
	return pulumix.Output[LookupLifecycleHookResult]{
		OutputState: o.OutputState,
	}
}

// The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are CONTINUE and ABANDON (default).
func (o LookupLifecycleHookResultOutput) DefaultResult() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLifecycleHookResult) *string { return v.DefaultResult }).(pulumi.StringPtrOutput)
}

// The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default value is 3600 seconds (1 hour). If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult property.
func (o LookupLifecycleHookResultOutput) HeartbeatTimeout() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupLifecycleHookResult) *int { return v.HeartbeatTimeout }).(pulumi.IntPtrOutput)
}

// The instance state to which you want to attach the lifecycle hook.
func (o LookupLifecycleHookResultOutput) LifecycleTransition() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLifecycleHookResult) *string { return v.LifecycleTransition }).(pulumi.StringPtrOutput)
}

// Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.
func (o LookupLifecycleHookResultOutput) NotificationMetadata() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLifecycleHookResult) *string { return v.NotificationMetadata }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. You can specify an Amazon SQS queue or an Amazon SNS topic. The notification message includes the following information: lifecycle action token, user account ID, Auto Scaling group name, lifecycle hook name, instance ID, lifecycle transition, and notification metadata.
func (o LookupLifecycleHookResultOutput) NotificationTargetArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLifecycleHookResult) *string { return v.NotificationTargetArn }).(pulumi.StringPtrOutput)
}

// The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.
func (o LookupLifecycleHookResultOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLifecycleHookResult) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLifecycleHookResultOutput{})
}

// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ivschat

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The state of the logging configuration. When the state is ACTIVE, the configuration is ready to log chat content.
type LoggingConfigurationStateEnum string

const (
	LoggingConfigurationStateEnumCreating       = LoggingConfigurationStateEnum("CREATING")
	LoggingConfigurationStateEnumCreateFailed   = LoggingConfigurationStateEnum("CREATE_FAILED")
	LoggingConfigurationStateEnumDeleting       = LoggingConfigurationStateEnum("DELETING")
	LoggingConfigurationStateEnumDeleteFailed   = LoggingConfigurationStateEnum("DELETE_FAILED")
	LoggingConfigurationStateEnumUpdating       = LoggingConfigurationStateEnum("UPDATING")
	LoggingConfigurationStateEnumUpdatingFailed = LoggingConfigurationStateEnum("UPDATING_FAILED")
	LoggingConfigurationStateEnumActive         = LoggingConfigurationStateEnum("ACTIVE")
)

type LoggingConfigurationStateEnumOutput struct{ *pulumi.OutputState }

func (LoggingConfigurationStateEnumOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LoggingConfigurationStateEnum)(nil)).Elem()
}

func (o LoggingConfigurationStateEnumOutput) ToLoggingConfigurationStateEnumOutput() LoggingConfigurationStateEnumOutput {
	return o
}

func (o LoggingConfigurationStateEnumOutput) ToLoggingConfigurationStateEnumOutputWithContext(ctx context.Context) LoggingConfigurationStateEnumOutput {
	return o
}

func (o LoggingConfigurationStateEnumOutput) ToLoggingConfigurationStateEnumPtrOutput() LoggingConfigurationStateEnumPtrOutput {
	return o.ToLoggingConfigurationStateEnumPtrOutputWithContext(context.Background())
}

func (o LoggingConfigurationStateEnumOutput) ToLoggingConfigurationStateEnumPtrOutputWithContext(ctx context.Context) LoggingConfigurationStateEnumPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v LoggingConfigurationStateEnum) *LoggingConfigurationStateEnum {
		return &v
	}).(LoggingConfigurationStateEnumPtrOutput)
}

func (o LoggingConfigurationStateEnumOutput) ToOutput(ctx context.Context) pulumix.Output[LoggingConfigurationStateEnum] {
	return pulumix.Output[LoggingConfigurationStateEnum]{
		OutputState: o.OutputState,
	}
}

func (o LoggingConfigurationStateEnumOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o LoggingConfigurationStateEnumOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e LoggingConfigurationStateEnum) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o LoggingConfigurationStateEnumOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o LoggingConfigurationStateEnumOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e LoggingConfigurationStateEnum) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type LoggingConfigurationStateEnumPtrOutput struct{ *pulumi.OutputState }

func (LoggingConfigurationStateEnumPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LoggingConfigurationStateEnum)(nil)).Elem()
}

func (o LoggingConfigurationStateEnumPtrOutput) ToLoggingConfigurationStateEnumPtrOutput() LoggingConfigurationStateEnumPtrOutput {
	return o
}

func (o LoggingConfigurationStateEnumPtrOutput) ToLoggingConfigurationStateEnumPtrOutputWithContext(ctx context.Context) LoggingConfigurationStateEnumPtrOutput {
	return o
}

func (o LoggingConfigurationStateEnumPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*LoggingConfigurationStateEnum] {
	return pulumix.Output[*LoggingConfigurationStateEnum]{
		OutputState: o.OutputState,
	}
}

func (o LoggingConfigurationStateEnumPtrOutput) Elem() LoggingConfigurationStateEnumOutput {
	return o.ApplyT(func(v *LoggingConfigurationStateEnum) LoggingConfigurationStateEnum {
		if v != nil {
			return *v
		}
		var ret LoggingConfigurationStateEnum
		return ret
	}).(LoggingConfigurationStateEnumOutput)
}

func (o LoggingConfigurationStateEnumPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o LoggingConfigurationStateEnumPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *LoggingConfigurationStateEnum) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// Specifies the fallback behavior if the handler does not return a valid response, encounters an error, or times out.
type RoomMessageReviewHandlerFallbackResult string

const (
	RoomMessageReviewHandlerFallbackResultAllow = RoomMessageReviewHandlerFallbackResult("ALLOW")
	RoomMessageReviewHandlerFallbackResultDeny  = RoomMessageReviewHandlerFallbackResult("DENY")
)

func (RoomMessageReviewHandlerFallbackResult) ElementType() reflect.Type {
	return reflect.TypeOf((*RoomMessageReviewHandlerFallbackResult)(nil)).Elem()
}

func (e RoomMessageReviewHandlerFallbackResult) ToRoomMessageReviewHandlerFallbackResultOutput() RoomMessageReviewHandlerFallbackResultOutput {
	return pulumi.ToOutput(e).(RoomMessageReviewHandlerFallbackResultOutput)
}

func (e RoomMessageReviewHandlerFallbackResult) ToRoomMessageReviewHandlerFallbackResultOutputWithContext(ctx context.Context) RoomMessageReviewHandlerFallbackResultOutput {
	return pulumi.ToOutputWithContext(ctx, e).(RoomMessageReviewHandlerFallbackResultOutput)
}

func (e RoomMessageReviewHandlerFallbackResult) ToRoomMessageReviewHandlerFallbackResultPtrOutput() RoomMessageReviewHandlerFallbackResultPtrOutput {
	return e.ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(context.Background())
}

func (e RoomMessageReviewHandlerFallbackResult) ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(ctx context.Context) RoomMessageReviewHandlerFallbackResultPtrOutput {
	return RoomMessageReviewHandlerFallbackResult(e).ToRoomMessageReviewHandlerFallbackResultOutputWithContext(ctx).ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(ctx)
}

func (e RoomMessageReviewHandlerFallbackResult) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e RoomMessageReviewHandlerFallbackResult) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e RoomMessageReviewHandlerFallbackResult) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e RoomMessageReviewHandlerFallbackResult) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type RoomMessageReviewHandlerFallbackResultOutput struct{ *pulumi.OutputState }

func (RoomMessageReviewHandlerFallbackResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RoomMessageReviewHandlerFallbackResult)(nil)).Elem()
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToRoomMessageReviewHandlerFallbackResultOutput() RoomMessageReviewHandlerFallbackResultOutput {
	return o
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToRoomMessageReviewHandlerFallbackResultOutputWithContext(ctx context.Context) RoomMessageReviewHandlerFallbackResultOutput {
	return o
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToRoomMessageReviewHandlerFallbackResultPtrOutput() RoomMessageReviewHandlerFallbackResultPtrOutput {
	return o.ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(context.Background())
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(ctx context.Context) RoomMessageReviewHandlerFallbackResultPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v RoomMessageReviewHandlerFallbackResult) *RoomMessageReviewHandlerFallbackResult {
		return &v
	}).(RoomMessageReviewHandlerFallbackResultPtrOutput)
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToOutput(ctx context.Context) pulumix.Output[RoomMessageReviewHandlerFallbackResult] {
	return pulumix.Output[RoomMessageReviewHandlerFallbackResult]{
		OutputState: o.OutputState,
	}
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e RoomMessageReviewHandlerFallbackResult) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o RoomMessageReviewHandlerFallbackResultOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e RoomMessageReviewHandlerFallbackResult) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type RoomMessageReviewHandlerFallbackResultPtrOutput struct{ *pulumi.OutputState }

func (RoomMessageReviewHandlerFallbackResultPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RoomMessageReviewHandlerFallbackResult)(nil)).Elem()
}

func (o RoomMessageReviewHandlerFallbackResultPtrOutput) ToRoomMessageReviewHandlerFallbackResultPtrOutput() RoomMessageReviewHandlerFallbackResultPtrOutput {
	return o
}

func (o RoomMessageReviewHandlerFallbackResultPtrOutput) ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(ctx context.Context) RoomMessageReviewHandlerFallbackResultPtrOutput {
	return o
}

func (o RoomMessageReviewHandlerFallbackResultPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*RoomMessageReviewHandlerFallbackResult] {
	return pulumix.Output[*RoomMessageReviewHandlerFallbackResult]{
		OutputState: o.OutputState,
	}
}

func (o RoomMessageReviewHandlerFallbackResultPtrOutput) Elem() RoomMessageReviewHandlerFallbackResultOutput {
	return o.ApplyT(func(v *RoomMessageReviewHandlerFallbackResult) RoomMessageReviewHandlerFallbackResult {
		if v != nil {
			return *v
		}
		var ret RoomMessageReviewHandlerFallbackResult
		return ret
	}).(RoomMessageReviewHandlerFallbackResultOutput)
}

func (o RoomMessageReviewHandlerFallbackResultPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o RoomMessageReviewHandlerFallbackResultPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *RoomMessageReviewHandlerFallbackResult) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// RoomMessageReviewHandlerFallbackResultInput is an input type that accepts RoomMessageReviewHandlerFallbackResultArgs and RoomMessageReviewHandlerFallbackResultOutput values.
// You can construct a concrete instance of `RoomMessageReviewHandlerFallbackResultInput` via:
//
//	RoomMessageReviewHandlerFallbackResultArgs{...}
type RoomMessageReviewHandlerFallbackResultInput interface {
	pulumi.Input

	ToRoomMessageReviewHandlerFallbackResultOutput() RoomMessageReviewHandlerFallbackResultOutput
	ToRoomMessageReviewHandlerFallbackResultOutputWithContext(context.Context) RoomMessageReviewHandlerFallbackResultOutput
}

var roomMessageReviewHandlerFallbackResultPtrType = reflect.TypeOf((**RoomMessageReviewHandlerFallbackResult)(nil)).Elem()

type RoomMessageReviewHandlerFallbackResultPtrInput interface {
	pulumi.Input

	ToRoomMessageReviewHandlerFallbackResultPtrOutput() RoomMessageReviewHandlerFallbackResultPtrOutput
	ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(context.Context) RoomMessageReviewHandlerFallbackResultPtrOutput
}

type roomMessageReviewHandlerFallbackResultPtr string

func RoomMessageReviewHandlerFallbackResultPtr(v string) RoomMessageReviewHandlerFallbackResultPtrInput {
	return (*roomMessageReviewHandlerFallbackResultPtr)(&v)
}

func (*roomMessageReviewHandlerFallbackResultPtr) ElementType() reflect.Type {
	return roomMessageReviewHandlerFallbackResultPtrType
}

func (in *roomMessageReviewHandlerFallbackResultPtr) ToRoomMessageReviewHandlerFallbackResultPtrOutput() RoomMessageReviewHandlerFallbackResultPtrOutput {
	return pulumi.ToOutput(in).(RoomMessageReviewHandlerFallbackResultPtrOutput)
}

func (in *roomMessageReviewHandlerFallbackResultPtr) ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(ctx context.Context) RoomMessageReviewHandlerFallbackResultPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(RoomMessageReviewHandlerFallbackResultPtrOutput)
}

func (in *roomMessageReviewHandlerFallbackResultPtr) ToOutput(ctx context.Context) pulumix.Output[*RoomMessageReviewHandlerFallbackResult] {
	return pulumix.Output[*RoomMessageReviewHandlerFallbackResult]{
		OutputState: in.ToRoomMessageReviewHandlerFallbackResultPtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RoomMessageReviewHandlerFallbackResultInput)(nil)).Elem(), RoomMessageReviewHandlerFallbackResult("ALLOW"))
	pulumi.RegisterInputType(reflect.TypeOf((*RoomMessageReviewHandlerFallbackResultPtrInput)(nil)).Elem(), RoomMessageReviewHandlerFallbackResult("ALLOW"))
	pulumi.RegisterOutputType(LoggingConfigurationStateEnumOutput{})
	pulumi.RegisterOutputType(LoggingConfigurationStateEnumPtrOutput{})
	pulumi.RegisterOutputType(RoomMessageReviewHandlerFallbackResultOutput{})
	pulumi.RegisterOutputType(RoomMessageReviewHandlerFallbackResultPtrOutput{})
}

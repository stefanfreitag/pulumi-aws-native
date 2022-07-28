// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Inputs
{

    public sealed class UserPoolAccountRecoverySettingArgs : global::Pulumi.ResourceArgs
    {
        [Input("recoveryMechanisms")]
        private InputList<Inputs.UserPoolRecoveryOptionArgs>? _recoveryMechanisms;
        public InputList<Inputs.UserPoolRecoveryOptionArgs> RecoveryMechanisms
        {
            get => _recoveryMechanisms ?? (_recoveryMechanisms = new InputList<Inputs.UserPoolRecoveryOptionArgs>());
            set => _recoveryMechanisms = value;
        }

        public UserPoolAccountRecoverySettingArgs()
        {
        }
        public static new UserPoolAccountRecoverySettingArgs Empty => new UserPoolAccountRecoverySettingArgs();
    }
}

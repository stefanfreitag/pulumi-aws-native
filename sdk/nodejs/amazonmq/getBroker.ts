// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AmazonMQ::Broker
 */
export function getBroker(args: GetBrokerArgs, opts?: pulumi.InvokeOptions): Promise<GetBrokerResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:amazonmq:getBroker", {
        "id": args.id,
    }, opts);
}

export interface GetBrokerArgs {
    id: string;
}

export interface GetBrokerResult {
    readonly amqpEndpoints?: string[];
    readonly arn?: string;
    readonly autoMinorVersionUpgrade?: boolean;
    readonly configuration?: outputs.amazonmq.BrokerConfigurationId;
    readonly configurationId?: string;
    readonly configurationRevision?: number;
    readonly dataReplicationMode?: string;
    readonly dataReplicationPrimaryBrokerArn?: string;
    readonly engineVersion?: string;
    readonly hostInstanceType?: string;
    readonly id?: string;
    readonly ipAddresses?: string[];
    readonly ldapServerMetadata?: outputs.amazonmq.BrokerLdapServerMetadata;
    readonly logs?: outputs.amazonmq.BrokerLogList;
    readonly maintenanceWindowStartTime?: outputs.amazonmq.BrokerMaintenanceWindow;
    readonly mqttEndpoints?: string[];
    readonly openWireEndpoints?: string[];
    readonly securityGroups?: string[];
    readonly stompEndpoints?: string[];
    readonly tags?: outputs.Tag[];
    readonly users?: outputs.amazonmq.BrokerUser[];
    readonly wssEndpoints?: string[];
}
/**
 * Resource Type definition for AWS::AmazonMQ::Broker
 */
export function getBrokerOutput(args: GetBrokerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetBrokerResult> {
    return pulumi.output(args).apply((a: any) => getBroker(a, opts))
}

export interface GetBrokerOutputArgs {
    id: pulumi.Input<string>;
}

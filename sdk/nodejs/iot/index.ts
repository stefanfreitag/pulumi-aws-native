// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./accountAuditConfiguration";
export * from "./authorizer";
export * from "./certificate";
export * from "./customMetric";
export * from "./dimension";
export * from "./domainConfiguration";
export * from "./fleetMetric";
export * from "./mitigationAction";
export * from "./provisioningTemplate";
export * from "./scheduledAudit";
export * from "./securityProfile";
export * from "./topicRule";
export * from "./topicRuleDestination";

// Export enums:
export * from "../types/enums/iot";

// Import resources to register:
import { AccountAuditConfiguration } from "./accountAuditConfiguration";
import { Authorizer } from "./authorizer";
import { Certificate } from "./certificate";
import { CustomMetric } from "./customMetric";
import { Dimension } from "./dimension";
import { DomainConfiguration } from "./domainConfiguration";
import { FleetMetric } from "./fleetMetric";
import { MitigationAction } from "./mitigationAction";
import { ProvisioningTemplate } from "./provisioningTemplate";
import { ScheduledAudit } from "./scheduledAudit";
import { SecurityProfile } from "./securityProfile";
import { TopicRule } from "./topicRule";
import { TopicRuleDestination } from "./topicRuleDestination";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:iot:AccountAuditConfiguration":
                return new AccountAuditConfiguration(name, <any>undefined, { urn })
            case "aws-native:iot:Authorizer":
                return new Authorizer(name, <any>undefined, { urn })
            case "aws-native:iot:Certificate":
                return new Certificate(name, <any>undefined, { urn })
            case "aws-native:iot:CustomMetric":
                return new CustomMetric(name, <any>undefined, { urn })
            case "aws-native:iot:Dimension":
                return new Dimension(name, <any>undefined, { urn })
            case "aws-native:iot:DomainConfiguration":
                return new DomainConfiguration(name, <any>undefined, { urn })
            case "aws-native:iot:FleetMetric":
                return new FleetMetric(name, <any>undefined, { urn })
            case "aws-native:iot:MitigationAction":
                return new MitigationAction(name, <any>undefined, { urn })
            case "aws-native:iot:ProvisioningTemplate":
                return new ProvisioningTemplate(name, <any>undefined, { urn })
            case "aws-native:iot:ScheduledAudit":
                return new ScheduledAudit(name, <any>undefined, { urn })
            case "aws-native:iot:SecurityProfile":
                return new SecurityProfile(name, <any>undefined, { urn })
            case "aws-native:iot:TopicRule":
                return new TopicRule(name, <any>undefined, { urn })
            case "aws-native:iot:TopicRuleDestination":
                return new TopicRuleDestination(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "iot", _module)
